import matplotlib.pyplot as plt
import numpy as np
from Technical import Technical

symbol = 'aapl'
n = 1000

prices_resp = Technical.get_historical_prices(symbol)[-n:]
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
x = np.arange(len(prices)-len(upper_bands), len(upper_bands)+(len(prices)-len(upper_bands)))
plt.plot(x, upper_bands, label='upper_band')
plt.plot(x, middle_bands, label='middle_band')
plt.plot(x, lower_bands, label='lower_band')

plt.xlabel('last '+str(n)+' days')
plt.ylabel('price')

plt.title("Plot of "+symbol)

plt.legend()

plt.show()