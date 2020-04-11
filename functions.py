import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib
import matplotlib.pyplot as plt
yf.pdr_override()

def SaveData(df,filename):
	df.to_csv(filename+'.csv')
	print("data saved to: " + str(filename) +'.csv')

def GetData(ticker,save,datefrom,dateto):
	print(ticker)
	data = pdr.DataReader(ticker,start=datefrom,end=dateto,data_source='yahoo')
	if save == True:
		dataname = ticker+'_'+str(dateto)
		SaveData(data,dataname)
	return data

def PrintPlot(data,parameter): 
	#function to create a plot from data and print it
	print("Displaying plot")
	data[parameter].plot(legend=True)
	plt.show()