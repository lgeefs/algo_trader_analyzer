import sys, os
from bs4 import BeautifulSoup
import requests
import csv

class SymbolScraper(object):

    def __init__(self):

        exchanges = [
            "AMEX",
            "NASDAQ",
            "NYSE",
            "TSX",
            "TSXV"
        ]

        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        symbols = []

        for exchange in exchanges:
            print(exchange)
            for letter in alphabet:
                print(letter)
                scraped_symbols = self.scrape(exchange, letter)
                symbols += scraped_symbols
            
        self.write_to_csv(symbols)


    def scrape(self, exchange, letter):

        canner = "http://www.eoddata.com/stocklist/"+exchange+"/"+letter+".htm"
        can = requests.get(canner)
        soup = BeautifulSoup(can.content, 'html.parser')
        bowls = soup.findAll(True, {'class':['re', 'ro']})
        symbols = []
        for b in bowls:
            symbol = b.find('a').get_text()
            symbols.append(symbol)
        return symbols

    def write_to_csv(self, symbols):
        with open('symbols.csv', 'w+') as csv_file:
            for s in symbols:
                csv_file.write(s)
                csv_file.write('\n')
        
        csv_file.close()
        
    
