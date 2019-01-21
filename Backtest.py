import datetime as datetime
from Account import Account
from Technical import Technical
from Analyzer import Analyzer
import os
import time

class Backtest(object):

    def __init__(self, strategy, symbol, n):

        print("Starting backtest for "+symbol+" using "+strategy)

        self.start_time = time.time()

        self._account = Account()

        prices = Technical.get_historical_prices(symbol)[-n:]

        method_to_use = getattr(self, strategy)

        result = method_to_use(prices)

        self.backtest(symbol, result, prices, method_to_use.__name__)

    def strat(self, prices):

        result = []

        

        return result

    def bb_strat(self, prices):
        upper_results = Analyzer.cross_upper_bb(prices)
        lower_results = Analyzer.cross_lower_bb(prices)

        result = []

        for i in range(0, len(upper_results)):
            #upper bands
            if upper_results[i] and not upper_results[i-1]:
                result.append('b')
            elif not upper_results[i] and upper_results[i-1]:
                result.append('h')
            #lower bands
            elif lower_results[i] and not lower_results[i-1]:
                result.append('s')
            elif not lower_results[i] and lower_results[i-1]:
                result.append('h')

            #else
            else:
                result.append('h')

        return result

    def backtest(self, symbol, indicators, prices, strategy):
        closes = [p['close'] for p in prices]

        #symbol = 'aapl'

        for i in range(0, len(indicators)):
            if indicators[i] == 'b':
                self._account.buy(symbol, 15, closes[i])
            elif indicators[i] == 's':
                self._account.sell(symbol, 15, closes[i])

        self._account.liquidate(symbol, closes[i])

        result = {
            'balance':self._account._balance,
            'shares':self._account._quantity
        }

        exec_time = time.time() - self.start_time
        print(symbol+" backtest ("+str(strategy)+") took "+exec_time+" to execute")

        ##################
        ## write to csv ##
        ##################

        d = datetime.date.today()
        # get abs path of directory by splitting abspath (directory | filename.ext)
        directory, _ = os.path.split(os.path.abspath(__file__))

        f = open(directory+'/backtests/logs/backtest_log.csv','a+')
        f.write(symbol+',')
        f.write(str(strategy)+',')
        f.write(str(len(closes))+',')
        f.write(str(d)+',')
        f.write(str(self._account._balance)+',')
        f.write(str(self._account._quantity)+',')
        f.write(str(len(indicators))+'\n')
        f.close()

        e = open(directory+'/backtests/logs/'+symbol+'_backtest_log.csv','a+')
        '''
        e.write(symbol+',')
        e.write(str(strategy)+',')
        e.write(str(d)+',')
        e.write(str(self._account._balance)+',')
        e.write(str(self._account._quantity)+'\n')
        '''
        for b in self._account._balances:
            e.write(str(b)+'\n')
        e.close()

        g = open(directory+'/backtests/results/'+symbol+'_backtest_result.csv', 'a+')
        g.write(symbol+',')
        g.write(str(strategy)+',')
        g.write(str(len(closes))+',')
        g.write(str(d)+',')
        g.write(str(self._account._balance)+',')
        g.write(str(self._account._quantity)+',')
        g.write(str(len(indicators))+'\n')
        g.close()

        return result
