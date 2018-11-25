import matplotlib.pyplot as plt
import numpy as np
from Technical import Technical

class Charter(object):

    def plot_macd(self, symbol, range):
        prices_resp = Technical.get_historical_prices(symbol)[-range:]
        prices = [p['close'] for p in prices_resp]

        macd_resp = Technical.get_macd(prices, 12, 26, 9)

        fasts = macd_resp['fasts']
        slows = macd_resp['slows']
        macds = macd_resp['macds']
        signal_line = macd_resp['signal_line']

        fasts = np.array(fasts)
        slows = np.array(slows)
        macds = np.array(macds)
        signal_line = np.array(signal_line)

        x = np.arange(0, len(macds))
        #plt.plot(x, fasts, label='fast ema')
        #plt.plot(x, slows, label='slow ema')
        plt.plot(x, macds, label='macd')
        x = np.arange(len(macds) - len(signal_line), len(macds))
        plt.plot(x, signal_line, label='signal')

        plt.xlabel('last '+str(range)+' days')
        plt.ylabel('price')

        plt.title("Plot of "+symbol)

        plt.legend()

        plt.savefig(symbol+' macd.png')

        plt.show()

    def plot_bollinger_bands(self, symbol, range):
        prices_resp = Technical.get_historical_prices(symbol)[-range:]
        prices = [p['close'] for p in prices_resp]

        bbands_resp = Technical.get_bollinger_bands(prices)

        upper_bands = [b['upper_band'] for b in bbands_resp]
        middle_bands = [b['middle_band'] for b in bbands_resp]
        lower_bands = [b['lower_band'] for b in bbands_resp]

        prices = np.array(prices)
        upper_bands = np.array(upper_bands)
        middle_bands = np.array(middle_bands)
        lower_bands = np.array(lower_bands)

        x = np.arange(0, len(prices))
        plt.plot(x, prices, label='price')
        x = np.arange(len(prices)-len(upper_bands), len(prices))
        plt.plot(x, upper_bands, label='upper_band')
        plt.plot(x, middle_bands, label='middle_band')
        plt.plot(x, lower_bands, label='lower_band')

        plt.xlabel('last '+str(range)+' days')
        plt.ylabel('price')

        plt.title("Plot of "+symbol)

        plt.legend()

        plt.savefig(symbol+' bbands.png')

        plt.show()

        #plt.savefig('/Applications/MAMP/htdocs/algo_trader_analyzer/'+symbol)