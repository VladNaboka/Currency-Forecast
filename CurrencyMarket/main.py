from tkinter import *
import inline as inline
import matplotlib
import openpyxl
from openpyxl import load_workbook
import datetime
import pandas as pa
import matplotlib as pyplot
from pandas import read_csv
import matplotlib.pyplot as plt
from pandas import read_excel
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def GetData(fileName):
    return read_excel(fileName)
    # return read_excel(fileName, header=0, parse_dates=[0], index_col=0)

exchangeEUR = GetData('eur_kzt-(нацбанк-республики-казахстан).xlsx')
exchangeUSD = GetData('usd_kzt-(нацбанк-республики-казахстан).xlsx')
exchangeRUB = GetData('rub_kzt-(нацбанк-республики-казахстан).xlsx')
# print(exchangeRatesSeries.head(10))
# print(exchangeRatesSeries.describe())
def ShowPltEUR():
    # exchangeEUR.plot(x="Date", y=["EUR", "RUB", "USD"])
    exchangeEUR.plot(x="Date", y="EUR")
    plt.show()
def ShowPltUSD():
    exchangeUSD.plot(x="Date", y="USD", color="green")
    plt.show()
def ShowPltRUB():
    exchangeRUB.plot(x="Date", y="RUB", color="green")
    plt.show()
# dataX = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# dataX = exchangeRatesSeries.plot(color="green")
# m_y = exchangeRatesSeries.head(10)

# def plot():
#     fig = Figure(figsize=(5, 5), dpi=100)
#     y = m_y
#     x = dataX
#     plot1 = fig.add_subplot(111)
#     plot1.plot(x, y)
#     plot1.plot(figsize=(12, 6))
#     plot1.plot(style='r--')
#     canvas = FigureCanvasTkAgg(fig, master=window)
#     canvas.draw()
#     canvas.get_tk_widget().pack()
#     toolbar = NavigationToolbar2Tk(canvas, window)
#     toolbar.update()
#     canvas.get_tk_widget().pack()
window = Tk()
window.title("Валютный рынок казахстана")
window.geometry('400x300')

btnPlot = Button(master=window,
                     command=ShowPltEUR,
                     height=2,
                     width=10,
                     text="График EUR")
btnPlot.grid(column=1, row=0)

btnPlot = Button(master=window,
                     command=ShowPltUSD,
                     height=2,
                     width=10,
                     text="График USD")
btnPlot.grid(column=1, row=1)
btnPlot = Button(master=window,
                     command=ShowPltRUB,
                     height=2,
                     width=10,
                     text="График RUB")
btnPlot.grid(column=1, row=2)
window.mainloop()