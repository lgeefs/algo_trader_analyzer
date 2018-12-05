from Technical import Technical
from Analyzer import Analyzer
from Backtest import Backtest
import time

print('Starting...')
time_start = time.time()

symbols = [
    'aapl',
    'fb',
    'nvda',
    'tsla',
    'amzn',
    'nflx',
    'goog',
    'spy'
]

n = 1000

strategy = 'bb_strat'

for symbol in symbols:
    backtest = Backtest(strategy, symbol, n)

print('Finished!')
exec_time = time.time() - time_start
print('Total execution time: '+str(exec_time))
