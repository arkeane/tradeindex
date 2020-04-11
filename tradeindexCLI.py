#!/usr/bin/env python3
import argparse
from datetime import date
from functions import *


#settings
matplotlib.use('TkAgg') #set tkinter as matlib displayer
today = date.today()
yearplot = date(today.year-1,today.month,today.day)

#Arguments CLI
parser = argparse.ArgumentParser(description='Gather information about companies shares')
parser.add_argument('Ticker',
					metavar='ticker',
					type=str,
					help='Trade index (ticker) such as AAPL')
parser.add_argument('-o', 
					'--option',
					nargs='?',
					type=str, 
					default='Close',
					help='Insert the data value that you want Possible values are(default is "Close"): "High" "Low" "Open", "Close", "Adj Close"')
parser.add_argument('-d', 
					'--date',
					nargs='?',
					type=str, 
					default=yearplot,
					help='Insert a period value (default is 1 year): example 2020-02-01 will result in a plot from the first of February 2020')
parser.add_argument('-s', 
					'--save',
					action="store_true",
					help='Save data in a .csv file')
args = parser.parse_args()

input_ticker = args.Ticker
input_option = args.option
input_date = args.date	
input_save = args.save

PrintPlot(GetData(input_ticker,input_save,input_date,today),input_option)