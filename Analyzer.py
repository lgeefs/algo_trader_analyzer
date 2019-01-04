import numpy as np
from Technical import Technical
from Account import Account

class Analyzer(object):

    @staticmethod
    def cross_upper_bb(prices):
        prices = np.array([p['close'] for p in prices])
        upper_bands = [p['upper_band'] for p in Technical.get_bollinger_bands(prices)]
        arrdiff = len(prices) - len(upper_bands)
        result = prices[arrdiff:] > upper_bands
        return result

    @staticmethod
    def cross_lower_bb(prices):
        prices = np.array([p['close'] for p in prices])
        lower_bands = [p['lower_band'] for p in Technical.get_bollinger_bands(prices)]
        arrdiff = len(prices) - len(lower_bands)
        result = prices[arrdiff:] < lower_bands
        return result

    @staticmethod
    def cross_macd(prices):
        prices = np.array([p['close'] for p in prices])
        macds = [p['macd'] for p in Technical.get_bollinger_bands(prices)]
        print(macds)


