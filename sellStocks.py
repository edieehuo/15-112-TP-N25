from cmu_graphics import *
from player import Player
from spawn import *
from info import *
from decision import *

#INVESTMENT IMPORTS
from investment import *
from stocks import *
from deposits import *

def sellStocks_onScreenActivate(app):
    # Check if the player has a portfolio
    print('in Sell Stocks', app.playerPortfolio)
    if app.playerPortfolio and len(app.playerPortfolio.stocks) > 0:
        app.sellStockNum = None  # Will wait for user input
        app.sellStockOption = None  # Will wait for user to choose stock
    else:
        app.drawNothingToSell = True  # If portfolio is empty, show a message and allow them to return
        

def sellStocks_redrawAll(app):
    drawLabel("SELL STOCKS SCREEN", app.width / 2, 10, size=40, bold=True)
    if app.drawNothingToSell:
        drawLabel("Your portfolio is empty!", app.width / 2, app.height / 2 - 30, size=20, align='center')
        drawLabel("Press Enter to return to the previous screen", app.width / 2, app.height / 2, size=20, align='center')
   
    else:
        if app.sellStockNum is None:
            drawLabel("Choose stock to sell (by index):", app.width / 2, app.height / 2 - 50, size=20, align='center')
            for idx, (key, data) in enumerate(app.playerPortfolio.stocks.items()):
                drawLabel(f"{idx + 1}: {key[0]} with {data['numHeld']} stocks", app.width / 2, app.height / 2 + (idx * 30), size=20)
        elif app.sellStockOption is not None:
            # Ask how many stocks to sell from the chosen stock
            stockKey = list(app.playerPortfolio.stocks.keys())[app.sellStockOption - 1]
            drawLabel(f"How many of {stockKey[0]} (Price: {stockKey[0]}) do you want to sell?", app.width / 2, app.height / 2, size=20, align='center')
            drawLabel("Enter quantity to sell:", app.width / 2, app.height / 2 + 30, size=20, align='center')
    
def sellStocks_onKeyPress(app, key):
    if key.isdigit():  # Check if the key pressed is a digit (number)
        if app.sellStockNum is None:  # First step, selecting stock to sell
            stockInd = int(key) - 1
            if 0 <= stockInd < len(app.playerPortfolio.stocks):
                app.sellStockOption = stockInd + 1
            else:
                print("Invalid stock selection!")
        elif app.sellStockNum is None:
            # If the user is in the state of asking for stock quantity
            stockKey = list(app.playerPortfolio.stocks.keys())[app.sellStockOption - 1]
            stock = app.playerPortfolio.stocks[stockKey]
            sellAmount = int(key)
            if sellAmount <= stock['numHeld']:
                # Subtract the amount sold from portfolio
                stock['numHeld'] -= sellAmount
                stock['value'] = stock['numHeld'] * stockKey[0]  # Update total value
                app.money += stockKey[0] * sellAmount  # Add money to player's balance
                print(f"Sold {sellAmount} of {stockKey[0]}")
                app.sellStockNum = None  # Reset the input after selling
                setActiveScreen('decision')

    
    elif key == 'a' and app.sellStockOption is not None:  # Sell all stocks in the portfolio
        # Ask user if they want to sell everything
        totalVal = 0
        for key, stock in app.playerPortfolio.stocks.items():
            totalVal += stock['value']  # Add up all stock values in portfolio

        app.money += total_value  # Add the total portfolio value to the player's money
        print(f"All stocks sold for a total of ${totalVal}")
        setActiveScreen('decision')

    elif key == 'enter':
        setActiveScreen('stocks')