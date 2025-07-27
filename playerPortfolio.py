import sys
import random
from cmu_graphics import *

class Portfolio:
    def __init__(self, stockPrice, stockVolatility, numHeld):
    # def __init__(self):
        # Portfolio structure: mapping { (stockPrice, stockVolatility): {numHeld: numberHeld, value: totalValue} }
        self.stocks = dict()
        self.stockPrice = stockPrice
        self.stockVolatility = stockVolatility
        self.numHeld = numHeld

    def __repr__(self):
        return f'Price: {self.stockPrice}, Volatility: {self.stockVolatility} Shares: {self.numHeld} '
    def addStock(self, stockPrice, stockVolatility, buyStockNum):
        stockKey = (stockPrice, stockVolatility)
        print(stockKey)
        # Check if the stock already exists in portfolio
        # If stock already exists, add to the held stock count and update value
        if stockKey in self.stocks:
            self.stocks[stockKey]['numHeld'] += buyStockNum
            # Update the total value based on the new stock price with volatility
            self.stocks[stockKey]['value'] += buyStockNum * stockPrice
            print(self.stocks)
        else:
            # Otherwise, create a new stock entry with the new value considering volatility
            self.stocks[stockKey] = {'numHeld': buyStockNum,'value': stockPrice * buyStockNum}
            print(self.stocks)

    def getStockValue(self, stockPrice, stockVolatility):
            stockKey = (stockPrice, stockVolatility)
            if stockKey in self.stocks:
                return self.stocks[stockKey]['value']
            else:
                return None