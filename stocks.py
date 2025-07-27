from cmu_graphics import *
from playerPortfolio import *
from sellStocks import *
#--- Stocks Screen --------------------------------------------------------------------------------------
# Stocks Class: 
class stockInfo:
    def __init__(self, stockPrice, stockVolatility):
        self.stockPrice = stockPrice
        self.stockVolatility = stockVolatility

def stocks_onScreenActivate(app):  
    print('in stocksOnScreenActivate', app.playerPortfolio)
    pass

def stocks_redrawAll(app):
    # DECISION SCREEN STOCK INFO DRAWING 
    if app.screenName == 'decision':
        if app.drawStockInfo:
            drawLabel(f"Stock Price: ${app.stockInfo.stockPrice}", app.width/2, app.height/2 + 150, size=20)
            drawLabel(f"Stock Volatility: {app.stockInfo.stockVolatility}%", app.width/2, app.height/2 + 180, size=20)
            drawLabel(f"Press S To Hide Stock Market Info", app.width/2, app.height - 50, size=20)
        if not app.drawStockInfo:
            drawLabel(f"Press S To See Stock Market Info", app.width/2, app.height - 50, size=20)
    
    #ON STOCK SCREEN DRAWING
    if app.screenName == 'stocks':
        drawLabel("Stocks Screen", app.width/2, 10, size=40, bold=True)
        drawLabel(f"Stock Price: ${app.stockInfo.stockPrice}", app.width/2, app.height/2 - 150, size=20)
        drawLabel(f"Stock Volatility: {app.stockInfo.stockVolatility}%", app.width/2, app.height/2 - 180, size=20)

        drawLabel("Press B to Buy Stocks", app.width/2, app.height/2)
        drawLabel("Press S to Sell Stocks", app.width/2, app.height/2 + 50)

def stocks_onKeyPress(app, key):
    if key == 'b':
        setActiveScreen('buyStocks')
        pass 
    elif key == 's':
        setActiveScreen('sellStocks')
        pass
    elif key == 'space':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys