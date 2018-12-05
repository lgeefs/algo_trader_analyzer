import datetime as datetime
from Account import Account
from Technical import Technical
from Analyzer import Analyzer

class Backtest(object):

    def __init__(self, strategy, symbol, n):

        self._account = Account()

        prices = Technical.get_historical_prices(symbol)[-n:]

        method_to_use = getattr(self, strategy)

        result = method_to_use(prices)

        self.backtest(symbol, result, prices, method_to_use.__name__)

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

        d = datetime.date.today()

        f = open('backtests/backtest_log.csv','a+')
        f.write(symbol+',')
        f.write(str(strategy)+',')
        f.write(str(d)+',')
        f.write(str(self._account._balance)+',')
        f.write(str(self._account._quantity)+'\n')
        f.close()

        e = open('backtests/'+symbol+'_backtest_log.csv','a+')
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

        return result
