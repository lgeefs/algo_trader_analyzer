import sys
import os
from Technical import Technical
from Analyzer import Analyzer

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

print(Technical.get_adx(prices))