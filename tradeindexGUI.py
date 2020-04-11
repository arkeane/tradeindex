import tkinter as tk
from datetime import date
from functions import *

matplotlib.use('TkAgg')
today = date.today()
yearplot = date(today.year-1,today.month,today.day)
command_list = ["AAPL",yearplot,today,"Close",False] #default values

def _getvalue(entry,array,pos):
	test = entry
	command_list[pos]=entry

def _quit():
    root.quit()
    root.destroy()

root = tk.Tk()

label = tk.Label(root, text="TradeIndex", font=("Arial Bold", 30))
label.pack()

label = tk.Label(root, text="Insert trading index (ex. AAPL)")
label.pack()
tickerentry = tk.Entry(root)
tickerentry.pack()
button = tk.Button(root,text="Insert", command=lambda: _getvalue(tickerentry.get(),command_list,0))
button.pack()

label = tk.Label(root, text="From (ex. 2020-02-01, default is 1 year from today)")
label.pack()
datefromentry = tk.Entry(root)
datefromentry.pack()
button = tk.Button(root,text="Insert", command=lambda: _getvalue(datefromentry.get(),command_list,1))
button.pack()

label = tk.Label(root, text="To (default is today)")
label.pack()
datetoentry = tk.Entry(root)
datetoentry.pack()
button = tk.Button(root,text="Insert", command=lambda: _getvalue(datetoentry.get(),command_list,2))
button.pack()

label = tk.Label(root, text="Insert parameter (ex. High, Low etc..., default is Close)")
label.pack()
paramentry = tk.Entry(root)
paramentry.pack()
button = tk.Button(root,text="Insert", command=lambda: _getvalue(paramentry.get(),command_list,3))
button.pack()

var = tk.BooleanVar()
var.set(False)
chk = tk.Checkbutton(root, text="Save raw data to .csv file", variable=var, command=lambda: _getvalue(var.get(),command_list,4))
chk.pack()

button = tk.Button(root,text="Plot", command=lambda: PrintPlot(GetData(command_list[0],command_list[4],command_list[1],command_list[2]),command_list[3]))
button.pack()

button = tk.Button(master=root, text="Quit", command=_quit)
button.pack()

root.mainloop()