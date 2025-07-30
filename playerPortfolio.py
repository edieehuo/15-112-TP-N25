import sys
import random
from cmu_graphics import *
from sellStocks import *


class Portfolio:
    def __init__(self, stockPrice, stockVolatility, numHeld):
        self.stocks = dict()
        self.stockPrice = stockPrice
        self.stockVolatility = stockVolatility
        self.numHeld = numHeld
        self.numDiffStocks = len(self.stocks)

    def __hash__(self):
        return hash((self.stockPrice, self.stockVolatility))
    def __eq__(self,other):
        if isinstance(other, Portfolio):
            if self.stockPrice == other.stockPrice and self.stockVolatility == other.stockVolatility:
                return True 
        return False 
    def __repr__(self):
        result = []
        i = 0 
        for stock in self.stocks: 
            #stock index 
            i += 1 
            boughtPrice, volatility = stock
            result.append(i)
            print(boughtPrice, volatility)
        return f'{self.stocks}'
    
    def addStock(self, stockPrice, stockVolatility, buyStockNum):
        if self.numDiffStocks >= 14:
            pass #nomore than 14 stocks in basket at once
        stockKey = (stockPrice, stockVolatility)
        if stockKey in self.stocks:
            self.stocks[stockKey]['numHeld'] += buyStockNum
            self.stocks[stockKey]['oldValue'] += buyStockNum * stockPrice
            self.stocks[stockKey]['newValue'] = buyStockNum * stockPrice
            self.numDiffStocks = len(self.stocks)
        else:
            self.stocks[stockKey] = {'numHeld': buyStockNum,'oldValue': stockPrice * buyStockNum, 'newValue': buyStockNum * stockPrice}
            self.numDiffStocks = len(self.stocks)

    def getAllStockTuplesInList(self): 
        if self.numDiffStocks == 0:
            return 'No stocks'
        else: 
            stockList = list(self.stocks.keys())
            return stockList