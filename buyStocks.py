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

def buyStocks_redrawAll(app):
    drawLabel("BUY STOCKS SCREEN", app.width / 2, 10, size=40, bold=True)
    # If buyStockNum is None, prompt the user to input a number
    if app.buyStockNum is None:
        drawLabel("Choose between 0-9 to buy", app.width / 2, app.height / 2, size=30, align='center')
    else:
        drawLabel(f'Number of stocks to buy: {app.buyStockNum}', app.width / 2, app.height / 2, size=20, bold=True)
        drawLabel(f'Press b to buy. Remember, no backsies!', app.width / 2, app.height / 2 + 20, size=20, bold=True)
        if app.playerPortfolio != None:
            drawLabel(f'Your portfolio: {app.playerPortfolio}', app.width / 2, app.height / 2 + 50, size=20, align='center')

def buyStocks_onKeyPress(app, key):
    if key.isdigit():  # Check if the key pressed is a digit (number)
        app.buyStockNum = int(key)
    elif key == 'b' and app.buyStockNum is not None:  # If 'b' is pressed and buyStockNum is valid
        # Add the stock using the input number of stocks
        app.playerPortfolio.addStock(app.stockInfo.stockPrice, app.stockInfo.stockVolatility, app.buyStockNum)
        print(app.playerPortfolio)
        setActiveScreen('decision')
    elif key == 'space':
        setActiveScreen('decision')  # Move to the next screen when space is pressed

