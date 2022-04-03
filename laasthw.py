import pandas as pd
import numpy
import matplotlib.pyplot as plt
from pandas_datareader import data

#date of the stock ;

start= '2019-01-01'
end= '2021-12-31'

HEINEKEN= data.DataReader(name='HEIA.AS', data_source='yahoo', start=start, end=end)
BUD= data.DataReader(name='BUD', data_source='yahoo', start=start, end=end)
HEINEKEN.Close.plot(color="green")
BUD.Close.plot(color="yellow")
plt.show()
print(HEINEKEN.columns)

#In my graphs I have decided to use the close value which allows us to have the best look when it comes to
#comapring the stocks performance since the previous day—and closing prices.
#Thanks to the plotted graph, during period of time 22019-2021 we can observe how both companies reacted day-to-day to the COVID19.
#We can see that both of the companies had a significant drop in their closing value when COVID19 became well known around the world
#This decreasee has been follow by slow returning to the original stock price


