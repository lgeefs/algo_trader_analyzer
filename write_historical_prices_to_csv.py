import os
import sys
import requests
import csv

res = requests.get("http://127.0.0.1/algo_trader/api/get/historical_prices?symbol=aapl&range=5y")
res_json = res.json()

if len(res_json) < 1:
    exit

print(res_json)
exit

with open('test.csv', 'w') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(res_json[0].keys())
    for item in res_json:
        csv_file.writerow(item.values())
