# tradeindex

Python program to retrieve data from any given trading ticker code such as AAPL or BTC-USD

## How to Install

clone the repository, then install this python libraries if you don't have them yet: `tkinter` `matplotlib` `yfinance` `pandas` `pandas_datareader` `argparse`, you can download the with pip install.

## How to Use

There are 2 versions just run `python3 tradeindexGUI.py` for the graphical interface, if you want to use the command line interface you have to insert some commands, here's and example: `python3 tradeindexCLI.py BTC-USD -d 2020-01-01 -o "Close" -s`, this command will result in a plot for the bitcoin to usd value from 2020-01-01 till today and it will save all the data in a .csv file, if you want to see all possible commands run `python3 tradeindexCLI.py -h`
