from cmu_graphics import *
from player import Player
from spawn import *
from info import *
from decision import *

#INVESTMENT IMPORTS
from investment import *
from stocks import *
from deposits import *
from sellStocks import *


def buyStocks_onScreenActivate(app):
    app.buyStockNum = None  # Initialize as None, will wait for user input
    app.tooBroke = False 
    pass 

def buyStocks_redrawAll(app):
    drawLabel("BUY STOCKS SCREEN", app.width / 2, 10, size=40, bold=True)
    # If buyStockNum is None, prompt the user to input a number
    if app.buyStockNum is None:
        drawLabel("Choose between 0-9 to buy", app.width / 2, app.height / 2, size=30, align='center')
    else:
        drawLabel(f'Number of stocks to buy: {app.buyStockNum}', app.width / 2, app.height / 2, size=20, bold=True)
        drawLabel(f'Remember, no backsies! Press b to buy {app.buyStockNum} stocks.', app.width / 2, app.height / 2 + 20, size=20, bold=True)
        if app.playerPortfolio != None:
            drawLabel(f'Your portfolio: {app.playerPortfolio}', app.width / 2, app.height / 2 + 50, size=20, align='center')
    if app.tooBroke:
        drawLabel(f'Too broke to buy {app.buyStockNum} stocks.', app.width / 2, app.height / 2 + 80, size=20, bold=True)

def buyStocks_onKeyPress(app, key):
    if key.isdigit():  # Check if the key pressed is a digit (number)
        app.buyStockNum = int(key)
        app.tooBroke = False 

    elif key == 'b' and  app.buyStockNum is not None:
        if canBuy(app):  
            app.tooBroke = False 
            app.player.money -= app.stockInfo.stockPrice*app.buyStockNum 
            app.playerPortfolio.addStock(app.stockInfo.stockPrice, app.stockInfo.stockVolatility, app.buyStockNum)
            print(app.playerPortfolio)
            setActiveScreen('decision')
        if not canBuy(app): 
            app.tooBroke = True 
    else:
        pass

def canBuy(app): 
    print('buyStocks: canBuy', app.buyStockNum, app.stockInfo.stockPrice)
    value = app.buyStockNum * app.stockInfo.stockPrice
    print('buyStocks: canBuy', value)
    print('buyStocks: canBuy', app.player.money) 
    if value <= app.player.money:
        print(f'has this much {app.player.money},000 , want to buy {value} amount stocks')
        return True 
    return False 
