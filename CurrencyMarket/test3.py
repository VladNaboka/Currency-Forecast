import datetime

import matplotlib.pyplot as plt
from openpyxl import Workbook
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
from adtk.visualization import plot
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
warnings.filterwarnings("ignore")
# %run f2forecast.py

df = pd.read_excel('TestEx.xlsx', index_col="Date")
train = df['2016':'2021']
fit1 = ExponentialSmoothing(df, seasonal_periods=12, trend='add', seasonal='mul').fit()
ax = df.plot(figsize=(15,6), color='black', title="Прогноз методом Хольта Винтерса")
fit1.fittedvalues.plot(ax=ax, style='--', color='red')
fit1.forecast(12).plot(ax=ax, style='--', color='green')
plt.show()

