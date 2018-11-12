import sys
import os
from Technical import Technical

prices = [
    10, 15, 20, 25, 30, 35, 40, 20, 25, 30, 35, 40,
    10, 15, 20, 40, 20, 25, 15, 20, 25, 30, 35, 40,
    20, 25, 30, 35, 40, 10, 15, 20, 40, 20, 15, 15
    ]

#print(Technical.get_price_change(20, 25))
#print(Technical.get_sma(prices))
#print(Technical.get_ema(prices))
print(Technical.get_macd(prices, 10, 30, 7))