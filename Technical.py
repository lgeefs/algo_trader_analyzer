import math
import requests

class Technical(object):

    @staticmethod
    def get_historical_prices(symbol):
        res = requests.get("http://127.0.0.1/algo_trader/api/get/historical_prices?symbol="+symbol+"&range=5y")
        return res.json()

    # get % price change between 2 prices
    @staticmethod
    def get_price_change(close, prev_close):
        multiplier = 1 if close > prev_close else -1
        return multiplier * 100 * abs(1 - (close / prev_close))

    # get simple moving average
    @staticmethod
    def get_sma(prices):
        period = len(prices)
        total = 0.0
        i = 0
        for p in prices:
            if i == period: break
            total += float(p)
            i += 1
        #return total / float(len(prices))
        return total / period

    # get exponential moving average
    @staticmethod
    def get_ema(prices):
        period = len(prices)
        alpha = 2 / (period + 1)
        #emas = []
        ema = Technical.get_sma(prices)
        i = 0
        for p in prices:
            if i == period: break
            ema = ema + alpha * (p - ema)
            #emas.append(ema)

        return ema

    # get moving average convergence/divergence oscillator
    @staticmethod
    def get_macd(prices, fast, slow, signal):

        if slow > len(prices):
            print('idiot')
            return

        fast_emas = []
        slow_emas = []
        macds = []

        # get macd for prices
        for i in range(0,len(prices)-1-slow):
            
            fast_ema = Technical.get_ema(prices[i+(slow-fast):slow+i])
            slow_ema = Technical.get_ema(prices[i:slow+i])
            macd = fast_ema - slow_ema
            #once we get enough macd data, we can plot signal line (7 ema) against macd
            macds.append(macd)
            # we still want to plot these lines on the chart so we'll return them
            fast_emas.append(fast_ema)
            slow_emas.append(slow_ema)
        
        signal_period = 7 # 7ema
        signal_line = []

        # get signal line for macd
        for i in range(0, len(macds)-1-signal_period):
            signal = Technical.get_ema(macds[i:signal_period+i])
            signal_line.append(signal)

        
        return {
            'fasts':fast_emas,
            'slows':slow_emas,
            'macds':macds,
            'signal_line':signal_line
        }
    
    @staticmethod
    def get_standard_deviation(prices):
        period = len(prices)
        mean = sum(prices) / period
        result = 0.00
        for p in prices:
            x = (p - mean) ** 2
            result += x
        result = result / float(period)
        result = math.sqrt(result)
        return result
    
    @staticmethod
    def get_bollinger_bands(prices):
        period = 20

        bands = []
        
        for i in range(0, len(prices)-1-period):
            price_slices = prices[i:i+period]
            middle_band = sma = Technical.get_sma(price_slices)
            gap = Technical.get_standard_deviation(price_slices) * 2
            upper_band = sma + gap
            lower_band = sma - gap
            bb = {
                'price':prices[i+period],
                'upper_band':upper_band,
                'middle_band':middle_band,
                'lower_band':lower_band
            }
            bands.append(bb)
        
        return bands

    @staticmethod
    def get_rsi(prices):
        period = len(prices)

        price_changes = []

        #for i in range(1, len(prices)-1-period):
            #price_changes.append(Technical.get_price_change(prices[i, i-1))
 



