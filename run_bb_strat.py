#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

from Technical import Technical
from Analyzer import Analyzer
from Backtest import Backtest
import time

print('Starting...')
time_start = time.time()

symbols = Technical.get_all_symbols()
print(symbols)

n = 200

strategy = 'bb_strat'

for symbol in symbols:
    backtest = Backtest(strategy, symbol, n)

print('Finished!')
exec_time = time.time() - time_start
print('Total execution time: '+str(exec_time))
