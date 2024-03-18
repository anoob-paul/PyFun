import pandas_datareader as pdr
import datetime as dt


start_date = dt.datetime(2018,1,1)
end_date =dt.datetime.now()

data =pdr.get_nasdaq_symbols()
print(data)

# pdr.get_data_fred('GS10')
