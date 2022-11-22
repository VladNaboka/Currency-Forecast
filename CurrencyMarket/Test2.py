from openpyxl import Workbook
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from adtk.visualization import plot
import pandas as pd
import numpy as np
import statsmodels.api as sm
# %run f2forecast.py
import warnings
warnings.filterwarnings("ignore")

def metrics(real, forecast):
    if type(real) == pd.core.frame.DataFrame:
        real = real[real.columns[0]].values

    print("Тест на стационарность:")
    dftest = adfuller(real - forecast, autolag='AIC')
    print("\tT-статистика = {:.3f}".format(dftest[0]))
    print("\tP-значение = {:.3f}".format(dftest[1]))
    print("Критические значения :")
    for k, v in dftest[4].items():
        print(
            "\t{}: {} - Данные {} стационарны с вероятностью {}% процентов".format(k, v, "не" if v < dftest[0] else "",
                                                                                   100 - int(k[:-1])))

    # real=np.array(real[real.columns[0]].values)
    forecast = np.array(forecast)
    print('MAD:', round(abs(real - forecast).mean(), 4))
    print('MSE:', round(((real - forecast) ** 2).mean(), 4))
    print('MAPE:', round((abs(real - forecast) / real).mean(), 4))
    print('MPE:', round(((real - forecast) / real).mean(), 4))
    print('Стандартная ошибка:', round(((real - forecast) ** 2).mean() ** 0.5, 4))

df = pd.read_excel('TestEx.xlsx', index_col="Date")
train = df['2016':'2021']
# model = auto_arima(df, seasonal=True, m=12, trace=True, suppress_warnings=True, error_action="ignore", stepwise=True)
mod = sm.tsa.statespace.SARIMAX(df, order=(4,1,5))
result = mod.fit()
print(result.summary().tables[1])
# result.plot_diagnostics(figsize=(15, 12))
# plt.show()
# predict = result.get_prediction(start=pd.to_datetime('2016-02-01'))
# metrics(train['2016-02-01':], predict.predicted_mean)
# print(predict.predicted_mean[:10])
# forecast2 = result.predict(periods=12)
predict = result.get_prediction(start='2020', end='2022')
ax = train.plot(figsize=(15,6), color='black', title='Прогнозирование')
result.fittedvalues.plot(ax=ax, style='--', color='red')
predict.predicted_mean.plot(ax=ax, style='--', color='green')
plt.show()








