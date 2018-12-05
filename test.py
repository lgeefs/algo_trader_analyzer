import sys
import os
from Technical import Technical
from Analyzer import Analyzer
from Charter import Charter

symbol = 'aapl'

c = Charter()

prices = Technical.get_historical_prices(symbol)[-500:]

cross_low_bb = Analyzer.cross_lower_bb(prices)
cross_up_bb = Analyzer.cross_upper_bb(prices)

print(cross_low_bb)
print(cross_up_bb)
c.plot(cross_low_bb*100)
c.plot(cross_up_bb*100)
c.plot([p['close'] for p in prices[20:]])
c.show()


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