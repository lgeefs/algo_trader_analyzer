import math
import requests
import numpy as np

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
            total += p
            i += 1
        #return total / len(prices)
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
        for i in range(0,len(prices)-slow):
            
            fast_ema = Technical.get_ema(prices[i+(slow-fast):slow+i])
            slow_ema = Technical.get_ema(prices[i:slow+i])
            macd = fast_ema - slow_ema
            #once we get enough macd data, we can plot signal line (7 ema) against macd
            macds.append(macd)
            # we still want to plot these lines on the chart so we'll return them
            fast_emas.append(fast_ema)
            slow_emas.append(slow_ema)
        
        
        signal_line = []
        histograms = []

        # get signal line for macd
        for i in range(0, len(macds)-signal):
            sig = Technical.get_ema(macds[i:signal+i])
            signal_line.append(sig)
            histograms.append(macds[i+signal]-sig)

        
        return {
            'fasts':fast_emas,
            'slows':slow_emas,
            'macds':macds,
            'signal_line':signal_line,
            'histograms':histograms
        }
    
    @staticmethod
    def get_standard_deviation(prices):
        period = len(prices)
        mean = sum(prices) / period
        result = 0.00
        for p in prices:
            x = (p - mean) ** 2
            result += x
        result = result / period
        result = math.sqrt(result)
        return result

    # standard deviation uses squares to retain positive values
    # mean deviation uses absolute values to retain positive values
    @staticmethod
    def get_mean_deviation(prices):
        period = len(prices)
        mean = sum(prices) / period
        result = 0.00
        for p in prices:
            x = abs(p - mean)
            result += x
        result = result / period
        result = math.sqrt(result)
        return result
    
    @staticmethod
    def get_bollinger_bands(prices):
        period = 20

        bands = []
        
        for i in range(0, len(prices)-period):
            price_slices = prices[i:i+period]
            middle_band = Technical.get_sma(price_slices)
            gap = Technical.get_standard_deviation(price_slices) * 2
            upper_band = middle_band + gap
            lower_band = middle_band - gap
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
        period = 14

        price_changes = [0]

        for i in range(1, len(prices)):
            price_changes.append(prices[i] - prices[i-1])
        
        gains = []
        losses = []
        avg_gains = []
        avg_losses = []
        rs_array = []
        for i in range(0, len(price_changes)):

            if price_changes[i] >= 0:
                gains.append(price_changes[i])
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(price_changes[i]))

            if i >= period:
                avg_gain = sum(gains[i-period:i]) / period
                avg_loss = sum(losses[i-period:i]) / period

                avg_gains.append(avg_gain)
                avg_losses.append(avg_loss)

                if i == period:
                    rs_array.append(avg_gain / avg_loss)
                else:
                    prev_avg_gain = avg_gains[i-period-1]
                    prev_avg_loss = avg_losses[i-period-1]
                    rs = (((prev_avg_gain * 13) + gains[i])/14) / (((prev_avg_loss * 13) + losses[i])/14)
                    rs_array.append(rs)

        rsi_array = []
        for rs in rs_array:
            rsi = 100 - (100/(1+rs))
            rsi_array.append(rsi)
        
        return {
            'rsi':rsi_array,
            'prices':prices[-len(rsi_array):]
        }

    # make sure to pass in full prices response, not just the closing prices!
    @staticmethod
    def get_cci(prices_resp):
        highs = np.array([p['high'] for p in prices_resp])
        lows = np.array([p['low'] for p in prices_resp])
        closes = np.array([p['close'] for p in prices_resp])
        
        typical_prices = (highs + lows + closes) / 3

        #print(typical_prices)

        sma_period = 20 # standard
        ccis = []

        for i in range(0, len(typical_prices) - sma_period):
            price_slices = typical_prices[i:sma_period+i]
            sma = Technical.get_sma(price_slices)
            mean_deviation = Technical.get_mean_deviation(price_slices)
            cci = (typical_prices[i+sma_period] - sma) / (0.015 * mean_deviation)
            ccis.append(cci)
        
        return {
            'ccis':ccis
        }


    @staticmethod         
    def get_adx(prices):
        print(prices)

    @staticmethod         
    def get_ad(prices):
        print(prices)

    @staticmethod         
    def get_aroon(prices):
        print(prices)

    @staticmethod         
    def get_obv(prices):
        print(prices)

