from cmu_graphics import *
from player import *
# from spawn import *
from info import *
from decision import *

#INVESTMENT IMPORTS
from investment import *
from stocks import *

#------Sell Stocks Screen----------------------------------------------------------------------------------------------------------------------------

def sellStocks_onScreenActivate(app):
    app.sellAmount = 0 
    if app.playerPortfolio.numDiffStocks > 0:
        app.drawNothingToSell = False 
    if app.playerPortfolio.stocks == {}:
        print('entering nothing to sell')
        app.drawNothingToSell = True  # If portfolio is empty, show a message and allow them to return
        

def sellStocks_redrawAll(app):
    drawLabel("SELL STOCKS SCREEN", app.width / 2, 10, size=40, bold=True)
    if app.drawNothingToSell:
        drawNothingToSell(app)
    else:
        drawLabel("Which stock to sell:", app.width / 2, app.height / 2 - 50, size=20, align='center')

        #draw Portfolio 
        drawPortfolio(app)
        allStockTuples = app.playerPortfolio.getAllStockTuplesInList()
        stockList = list(app.playerPortfolio.stocks.items())
        print('sellStocks: redrawAll portfolio', app.playerPortfolio)
        print('sellStocks: redrawAll stocks',app.playerPortfolio.stocks)
        for i in range(len(allStockTuples)):
            stockKey, stockData = stockList[i] 
            strikePrice, volatility = stockKey
            numHeld = stockData['numHeld']
            drawLabel(f"{numHeld} Shares of Stock {i+1}: Bought For ${strikePrice} /share, \u03C3: {volatility}%", #\u03C3 is for sigma
                      app.width / 2, app.height / 2 + (i * 30), size=20)

        if app.sellStockNum is None:
            drawLabel(f"Selling stock:", 
                      app.width / 2, app.height / 2 + 150, size=20, align='center')
            drawLabel(f"Press C to Change Stock Selection", 
                      10, app.height / 2 + 150, size=20, align = 'left')
            
            drawLabel(f"Num To Sell: ",  
                      app.width / 2, app.height / 2 + 180, size=20, fill = 'gray')            
            drawLabel(f"Press 's' to sell- be certain! ",  
                      app.width / 2, app.height / 2 + 200, size=20)
        if app.sellStockNum is not None:
            drawLabel(f"Selling stock {app.sellStockNum + 1}", 
                      app.width / 2, app.height / 2 + 150, size=20)
            drawLabel(f"Press C to Change Stock Selection", 
                      10, app.height / 2 + 150, size=20, align = 'left')
            drawLabel(f"Num To Sell: {app.sellAmount}",  
                      app.width / 2, app.height / 2 + 180, size=20, align='center', fill = 'pink')            
            drawLabel(f"Press 's' to sell- be certain! ", 
                      app.width / 2, app.height / 2 + 200, size=20, align='center')

def drawNothingToSell(app):
    #draw bg 
    drawRect(0,0, app.width, app.height, fill = 'black')
    drawLabel("Portfolio is empty.", 
              app.width / 2, app.height / 2 - 30, 
              fill = 'lime', bold = True, size=20, align='center')
    drawLabel("Press Enter to return to Stock Market", 
              app.width / 2, app.height / 2, 
              fill = 'white', bold = True, size=20, align='center')

def sellStocks_onKeyPress(app, key):
    if app.drawNothingToSell:
        if key == 'enter':
            setActiveScreen('stocks')
    #Let user change stock 
    if app.sellStockNum is None:
        if key == 'c': 
            pass 
    #TEST-------------------------------------------
    if key == 'c':
        app.sellStockNum = None 
    
    #------------------------------------------------
    if key.isdigit():   # Check if the key pressed is a digit (number)
        if app.sellStockNum is None:  # First step, selecting stock to sell
            stockInd = int(key) - 1  # Convert the index to zero-based
            if 0 <= stockInd < len(app.playerPortfolio.stocks):
                app.sellStockNum = stockInd  # Store selected stock
            else:
                pass 
        elif app.sellStockNum != None:
            app.sellAmount = int(key)
            # if key == 'c':
            #     app.sellStockNum = None 
            print(f'sellStocks.py onKeyPress: sellAmount: {app.sellAmount}')


    if key == 's' and app.sellStockNum is not None: 

        allStockTuples = app.playerPortfolio.getAllStockTuplesInList()
        stockKey = allStockTuples[app.sellStockNum]
        stock = app.playerPortfolio.stocks[stockKey]

        if app.sellAmount <= stock['numHeld']:

            sellPricePerShare = app.playerPortfolio.stocks[stockKey]['newValue'] / app.playerPortfolio.stocks[stockKey]['numHeld']
            moneyFromSellingStocks = math.ceil(sellPricePerShare * app.sellAmount)
            app.player.money += moneyFromSellingStocks  # Add money to player's balance
            stock['numHeld'] -= app.sellAmount
            stock['oldValue'] = stock['numHeld'] * stockKey[0]  # Update total value

            if stock['numHeld'] == 0:
                app.playerPortfolio.stocks.pop(stockKey)

            #Reset input 
            app.log.insert(0,f'Made ${moneyFromSellingStocks} from Stocks')
            app.sellStockNum = None  
            app.sellAmount = 0
            
            setActiveScreen('decision')  # Go back to decision screen after sale
        else:
            setActiveScreen('sellStocks')
            print("Invalid number to sell.")
            pass
                    
    
    else:
        pass  


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