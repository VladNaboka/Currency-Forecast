import datetime
from openpyxl import Workbook
from pandas import read_csv
from pandas import read_excel
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_percentage_error
import statsmodels.api as sm
import pandas as pd
import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
warnings.simplefilter('ignore', ConvergenceWarning)

# get data
def GetData(fileName):
    return read_csv(fileName, header=0, parse_dates=[0], index_col=0).values
def GetDataExcel(fileName):
    return read_excel(fileName, header=0, parse_dates=[0], index_col=0).values
def GetDataExcelNull(fileName):
    return read_excel(fileName).values
# sm.tsa.arima.
# Function that calls ARIMA model to fit and forecast the data
def StartARIMAForecasting(Actual, P, D, Q):
    model = ARIMA(Actual, order=(P, D, Q))
    model_fit = model.fit()
    prediction = model_fit.forecast(1200)[0]
    return prediction

# Get exchange rates
ActualData = GetDataExcel('TestEx.xlsx')
# Size of exchange rates
NumberOfElements = len(ActualData)

# Use 70% of data as training, rest 30% to Test model
TrainingSize = int(NumberOfElements * 0.7)
TrainingData = ActualData[0:TrainingSize]
TestData = ActualData[TrainingSize:NumberOfElements]

# new arrays to store actual and predictions
Actual = [x for x in TrainingData]
Predictions = list()

# in a for loop, predict values using ARIMA model
for timepoint in range(len(TestData)):
    ActualValue = TestData[timepoint]
    # forcast value
    Prediction = StartARIMAForecasting(Actual, 3, 1, 0)
    print('Actual=%f, Predicted=%f' % (ActualValue, Prediction))
    # print(ActualValue)
    # add it in the list
    Predictions.append(Prediction)
    Actual.append(ActualValue)

# Print MSE to see how good the model is
Error = mean_absolute_percentage_error(TestData, Predictions)
print('Test Mean Squared Error (smaller the better fit): %.3f' % Error)
# plot
pyplot.title("Analytics")
pyplot.plot(TestData)
pyplot.plot(Predictions, color='red')
pyplot.show()