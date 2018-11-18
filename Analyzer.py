from Technical import Technical

class Analyzer(object):

    _prices = []

    def setup(self, symbol):
        print('Setup')
        self._prices = Technical.get_historical_prices(symbol)
        self.analyze()

    def analyze(self):
        print('Analyzing')
        closing_prices = [p['close'] for p in self._prices]
        print(closing_prices)
        self.finish()
        
    def finish(self):
        print('Finished')
    

