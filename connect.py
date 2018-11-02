import os
import sys
import requests

res = requests.get("http://127.0.0.1/algo_trader/api/get/historical_prices?symbol=aapl")

values = []

for j in reversed(res.json()):
    print(j)
    break
    
