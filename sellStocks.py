#print debugging statement :
print(f'in Sell Stocks on Screen Activate')

from cmu_graphics import *
from player import *
from spawn import *
from info import *
from decision import *

#INVESTMENT IMPORTS
from investment import *
from stocks import *
from deposits import *

def sellStocks_onScreenActivate(app):
    # Check if the player has a portfolio
    print('in Sell Stocks on Screen Activate', app.playerPortfolio)
    print('in Sell Stocks on ScreenActivate', app.playerPortfolio.numDiffStocks)
    if app.playerPortfolio.numDiffStocks > 0:
        print('entering player going to sell')
        app.drawNothingToSell = False 

        app.sellStockNum = None  # Will wait for user input
        app.sellStockOption = None  # Will wait for user to choose stock
    else:
        print('entering nothing to sell')
        app.drawNothingToSell = True  # If portfolio is empty, show a message and allow them to return
        

def sellStocks_redrawAll(app):
    drawLabel("SELL STOCKS SCREEN", app.width / 2, 10, size=40, bold=True)
    #this is fine 
    if app.drawNothingToSell:
        drawLabel("Your portfolio is empty!", app.width / 2, app.height / 2 - 30, size=20, align='center')
        drawLabel("Press Enter to return to the previous screen", app.width / 2, app.height / 2, size=20, align='center')
   
    else:
        if app.sellStockNum is None:
            drawLabel("Choose stock to sell (by index):", app.width / 2, app.height / 2 - 50, size=20, align='center')
            allStockTuples = app.playerPortfolio.getAllStockTuplesInList()
            for i in range(len(allStockTuples)):
                strikePrice, volatility = allStockTuples[i]
                #\u03C3 is for sigma, to stand for volatility. else string would be too long 
                drawLabel(f"Stock {i+1}: Bought For ${strikePrice} /share, \u03C3: {volatility}%", app.width / 2, app.height / 2 + (i * 30), size=20)
                drawLabel(f'Stock {i+1}: CurrVal', app.width / 2, app.height / 2 + (i * 30) + 20, size=20)
        elif app.sellStockOption is not None:
            # Ask how many stocks to sell from the chosen stock
            stockKey = list(app.playerPortfolio.stocks.keys())[app.sellStockOption - 1]
            drawLabel(f"How many of {stockKey[0]} (Price: {stockKey[0]}) do you want to sell?", app.width / 2, app.height / 2, size=20, align='center')
            drawLabel("Enter quantity to sell:", app.width / 2, app.height / 2 + 30, size=20, align='center')
    
def sellStocks_onKeyPress(app, key):
    if app.drawNothingToSell:
        if key == 'enter':
            setActiveScreen('stocks')
    if key.isdigit():  # Check if the key pressed is a digit (number)
        if app.sellStockNum is None:  # First step, selecting stock to sell
            stockInd = int(key) - 1  # Convert the index to zero-based
            if 0 <= stockInd < len(app.playerPortfolio.stocks):
                app.sellStockOption = stockInd + 1  # Store selected stock
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
                setActiveScreen('decision')  # Go back to decision screen after sale
            else:
                print("You don't have enough stock to sell!")
    
    elif key == 'return' and app.sellStockOption is not None:
        # Confirm sale when the user presses 'Enter'
        stockKey = list(app.playerPortfolio.stocks.keys())[app.sellStockOption - 1]
        stock = app.playerPortfolio.stocks[stockKey]
        sellAmount = app.sellStockNum  # The number of stocks to sell
        if sellAmount <= stock['numHeld']:
            stock['numHeld'] -= sellAmount
            stock['value'] = stock['numHeld'] * stockKey[0]
            app.money += stockKey[0] * sellAmount
            print(f"Sold {sellAmount} of {stockKey[0]}")
            app.sellStockNum = None
            setActiveScreen('decision')
        else:
            print("Not enough stock to sell.")
    
    elif key == 'space':
        setActiveScreen('decision') 