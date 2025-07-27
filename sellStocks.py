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

def sellStocks_onScreenActivate(app):
    if app.playerPortfolio.numDiffStocks > 0:
        app.drawNothingToSell = False 
    else:
        print('entering nothing to sell')
        app.drawNothingToSell = True  # If portfolio is empty, show a message and allow them to return
        

def sellStocks_redrawAll(app):
    drawLabel("SELL STOCKS SCREEN", app.width / 2, 10, size=40, bold=True)
    if app.drawNothingToSell:
        drawLabel("Your portfolio is empty!", app.width / 2, app.height / 2 - 30, size=20, align='center')
        drawLabel("Press Enter to return to the previous screen", app.width / 2, app.height / 2, size=20, align='center')
    else:
        drawLabel("Choose stock to sell (by index):", app.width / 2, app.height / 2 - 50, size=20, align='center')
        allStockTuples = app.playerPortfolio.getAllStockTuplesInList()
        for i in range(len(allStockTuples)):
            strikePrice, volatility = allStockTuples[i] 
            drawLabel(f"Stock {i+1}: Bought For ${strikePrice} /share, \u03C3: {volatility}%", #\u03C3 is for sigma
                      app.width / 2, app.height / 2 + (i * 30), size=20)
            drawLabel(f'Stock {i+1}: CurrVal', 
                      app.width / 2, app.height / 2 + (i * 30) + 20, size=20)
        if app.sellStockNum is not None:
            drawLabel(f"selling stock {app.sellStockNum + 1}, press c to change", 
                      app.width / 2, app.height / 2 + 150, size=20, align='center')

def sellStocks_onKeyPress(app, key):
    if app.drawNothingToSell:
        if key == 'enter':
            setActiveScreen('stocks')
    #let user change stock... 
    if key == 'c': 
        app.sellStockNum = None 

    if key.isdigit():  # Check if the key pressed is a digit (number)
        if app.sellStockNum is None:  # First step, selecting stock to sell
            stockInd = int(key) - 1  # Convert the index to zero-based
            if 0 <= stockInd < len(app.playerPortfolio.stocks):
                app.sellStockNum = stockInd  # Store selected stock
            else:
                pass 
        elif app.sellStockNum is not None:
            allStockTuples = app.playerPortfolio.getAllStockTuplesInList()
            stockKey = allStockTuples[app.sellStockNum]
            print(stockKey)
            stock = app.playerPortfolio.stocks[stockKey]
            sellAmount = int(key)
            print(f'sellStocks onKeyPress: sellAmount: {sellAmount}')
            if sellAmount <= stock['numHeld']:
                # Subtract the amount sold from portfolio
                stock['numHeld'] -= sellAmount
                stock['value'] = stock['numHeld'] * stockKey[0]  # Update total value
                app.money += stockKey[0] * sellAmount  # Add money to player's balance
                print(f"Sold {sellAmount} of {stockKey[0]}")
                if stock['numHeld'] == 0:
                    app.playerPortfolio.stocks.pop(stockKey)
                #Reset input 
                app.sellStockNum = None  
                setActiveScreen('decision')  # Go back to decision screen after sale
            else:
                print("Invalid number to sell.")
    
    else:
        pass  