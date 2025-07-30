from cmu_graphics import *
from player import Player
from info import *

#INVESTMENT IMPORTS
from investment import *
from stocks import *

def buyStocks_onScreenActivate(app):
    app.buyStockNum = None  # Initialize as None, will wait for user input
    app.tooBroke = False 
    pass 

def buyStocks_redrawAll(app):
    drawLabel("BUY STOCKS SCREEN", app.width / 2, 10, size=40, bold=True)
    # If buyStockNum is None, prompt the user to input a number
    if app.buyStockNum is None:
        drawLabel("You can buy between 0-9 stocks.",  app.width // 2, app.height // 2, size=30, align='center')
        drawLabel("How many do you want to buy?", app.width // 2, app.height // 2 + 40, size=30, align='center')
    else:
        drawLabel(f'Number of stocks to buy: {app.buyStockNum}', app.width / 2, app.height / 2, size=20, bold=True)
        drawLabel(f"No Backsies! Press 'b' to buy {app.buyStockNum} stocks.", app.width / 2, app.height / 2 + 20, size=20, bold=True)
        if app.playerPortfolio != None:
            drawPortfolio(app)
    if app.tooBroke:
        drawLabel(f'Cannot afford to buy {app.buyStockNum} stocks.', app.width / 2, app.height / 2 + 80, size=20, bold=True)

def buyStocks_onKeyPress(app, key):
    if key.isdigit():  # Check if the key pressed is a digit (number)
        app.buyStockNum = int(key)
        app.tooBroke = False 

    elif key == 'b' and  app.buyStockNum is not None:
        if canBuy(app):  
            app.tooBroke = False 
            app.log.insert(0,f'Invested ${app.invested} in Stocks')
            app.invested = 0 #resetting back to the beginning so that i don't have cray nums
            app.player.money -= app.stockInfo.stockPrice*app.buyStockNum 
            app.playerPortfolio.addStock(app.stockInfo.stockPrice, app.stockInfo.stockVolatility, app.buyStockNum)
            setActiveScreen('decision')
        if not canBuy(app): 
            app.tooBroke = True 
    else:
        pass

def canBuy(app): 
    # print('buyStocks: canBuy', app.buyStockNum, app.stockInfo.stockPrice)
    value = app.buyStockNum * app.stockInfo.stockPrice
    # print('buyStocks: canBuy', value)
    # print('buyStocks: canBuy', app.player.money) 
    if value <= app.player.money:
        app.invested = value 
        return True 
    return False 

def drawPortfolio(app): 
    boxX = 200 # right edge of tracker 
    boxY = 700 #where to stop 

    marketPlotX = boxX
    marketPlotY = boxY
    #variable 
    marketPlotHeight = 100

    holdX = marketPlotX
    holdY = marketPlotY + marketPlotHeight
    # print(app.playerPortfolio)
    # print(app.playerPortfolio.numDiffStocks)
    if app.playerPortfolio.numDiffStocks == 0: 
        # print('skipping in drawPort since drawPort is empty ')
        return 
    else: 
        i = 0
        iToMod = 0
        stockSpacing = 15
        stockColSpacing = 20
        stockColPadding = 20
        priceToSellPriceSpacing = 150
        for stock in app.playerPortfolio.stocks:
            i += 1
            buyPrice, vol = stock # don't need volatility to be drawn 
            newTotalValue = app.playerPortfolio.stocks[stock]['newValue']
            if app.playerPortfolio.stocks[stock]['numHeld'] != 0:
                sellPrice = newTotalValue //  app.playerPortfolio.stocks[stock]['numHeld']
            else:
                sellPrice = 'No Stocks Held'
            # print('drawPort buy', buyPrice)
            distBottomScreen = 10
            if holdY + i*stockSpacing <= app.height - distBottomScreen:
                iToMod += 1
                drawLabel(f"{i}: Buy Price ${buyPrice}", 
                          holdX + stockColPadding, 
                          holdY + i*stockSpacing, align = 'left',  
                          size = 15)
                drawLabel(f"Market Price ${sellPrice}", 
                          holdX + stockColPadding + priceToSellPriceSpacing, 
                          holdY + i*stockSpacing, align = 'left', 
                          size = 15)
            else: 
                drawLabel(f"{i}: Buy Price ${buyPrice}", 
                          holdX + stockColPadding*2 + stockColSpacing*3 + priceToSellPriceSpacing*2, 
                          holdY + (i%iToMod)*stockSpacing, align = 'left', 
                          size = 15)
                drawLabel(f"Market Price ${sellPrice}", 
                          holdX + stockColPadding*2 + stockColSpacing*4 + priceToSellPriceSpacing*3, 
                          holdY + (i%iToMod)*stockSpacing, align = 'left', 
                          size = 15)

    pass 