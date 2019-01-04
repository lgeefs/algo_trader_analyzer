import sys
import os
from Technical import Technical
from Analyzer import Analyzer
from Charter import Charter

print('starting test...')

symbol = 'aapl'
range = 20

y = 2018
i = 0

prices = []

while y < 2019:
    m = 10
    while m < 13:
        d = 1
        while d < 32:
            mon = m
            day = d
            if m < 10:
                mon = '0'+str(m)
            if d < 10:
                day = '0'+str(d)
            p = Technical.get_prices(symbol, str(y)+str(mon)+str(day))
            if len(p) > 0:
                prices.append(p)
            d+=1
        m+=1
    if i == 0:
        break
    i+=1
    y+=1

for p in prices:
    print(p['date'])



print('finished test!')

'''

prices = [
    10.63, 11.42, 11.11, 11.23, 11.44, 10.99, 12.45, 12.39, 11.90, 11.80,
    11.88, 12.01, 12.01, 12.14, 12.25, 12.20, 12.46, 11.41, 11.62, 11.33,
    11.45, 11.41, 11.20, 11.23, 11.12, 11.67, 11.59, 12.23, 12.45, 13.00,
    13.01, 12.77, 12.70, 13.15, 13.22, 13.46, 13.31, 13.33, 13.21, 12.99,
    12.87, 12.88, 12.01, 11.66, 11.70, 11.08, 10.88, 10.54, 10.77, 11.01
    ]

smas = Technical.get_sma(prices)
emas = Technical.get_ema(prices)
macds = Technical.get_macd(prices, 10, 30, 7)
std_dev = Technical.get_standard_deviation(prices)
bbands = Technical.get_bollinger_bands(prices)
rsi = Technical.get_rsi(prices)

prices = Technical.get_historical_prices('aapl')

n = 100
c = Charter()
c.plot_sma('aapl', n, 12)
c.plot_sma('aapl', n, 26)
c.plot_sma('aapl', n, 50)
c.plot_sma('aapl', n, 100)
c.plot_sma('aapl', n, 200)
c.plot_bollinger_bands('aapl', n)

c.show()

#print(Technical.get_adx(prices))
'''