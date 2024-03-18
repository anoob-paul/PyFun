import pandas_datareader as pdr
import datetime as dt



# data =pdr.get_data_yahoo()
data = pdr.DataReader('BTC-USD', 'yahoo', start='2019-9-10', end='2024-3-9')

print(data)

# pdr.get_data_fred('GS10')
