import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import datetime
# %matplotlib inline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_log_error


Tdata = pd.read_excel('TestEx.xlsx')
Tdata['Date'] = pd.to_datetime(Tdata['Date'])
Tdata.set_index('Date', inplace=True)
df = Tdata[['EUR']]
forecastOut = int(math.ceil(0.05 * len(df)))
# print(forecastOut)
df['label'] = df['EUR'].shift(-forecastOut)

scaler = StandardScaler()
x = np.array(df.drop(labels=['label'], axis=1))
scaler.fit(x)
x = scaler.transform(x)

PredictionsX = x[-forecastOut:]
X = x[:-forecastOut]

df.dropna(inplace=True)
y = np.array(df['label'])

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# randomf = RandomForestRegressor()
# randomf.fit(Xtrain, ytrain)
# rf_confidence = randomf.score(Xtest, ytest)
lr = LinearRegression()
lr.fit(Xtrain, ytrain)
lrConf = lr.score(Xtest, ytest)

lastDate = df.index[-1]
lastUnix = lastDate.timestamp()
oneDay = 86400
nextUn = lastUnix + oneDay
forecastSet = lr.predict(PredictionsX)
df['Forecast'] = np.nan
for i in forecastSet:
    nextDate = datetime.datetime.fromtimestamp(nextUn)
    nextUn += 86400 * 2
    df.loc[nextDate] = [np.nan for _ in range(len(df.columns)-1)]+[i]

plt.figure(figsize=(12, 6))
df['EUR'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.show()
