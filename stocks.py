from cmu_graphics import *
from playerPortfolio import *
from playerHoldingTracker import *
from sellStocks import *

#--------------------------------------------------------------------------------------------------------------------------------------------
#--- Stocks Screen --------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

# Class to hold stock information
class stockInfo:
    def __init__(self, stockPrice, stockVolatility):
        self.stockPrice = stockPrice
        self.stockVolatility = stockVolatility

# Called when stocks screen becomes active
def stocks_onScreenActivate(app):  
    # Button sizes
    buttonWidth = 180
    buttonHeight = 40
    spacing = 20
    totalHeight = 3 * buttonHeight + 2 * spacing

    # Top Y coordinate to vertically center the stack
    startY = (app.height // 2) - (totalHeight // 2)
    centerX = app.width // 2

    # Define buttons as rectangles (x, y, width, height)
    app.buyButton = (centerX - buttonWidth//2, startY, buttonWidth, buttonHeight)
    app.sellButton = (centerX - buttonWidth//2, startY + buttonHeight + spacing, buttonWidth, buttonHeight)
    app.returnButton = (centerX - buttonWidth//2, startY + 2*(buttonHeight + spacing), buttonWidth, buttonHeight)

# Draw the stocks screen layout
def stocks_redrawAll(app):
    # background 
    drawRect(0,0, app.width, app.height, fill = 'black')

    #draw portfolio 
    drawPortfolio(app)
    #draw marketplot 
    marketPlotX = 200
    marketPlotY = 110
    marketPlotWidth = 600
    #variable 
    marketPlotHeight = 200
    #draw line plot of market cond variable
    drawMarketPlot(app, marketPlotX, marketPlotY, marketPlotWidth, marketPlotHeight)

    # Draw Buttons
    drawButton(app.buyButton, "Buy Stocks")
    drawButton(app.sellButton, "Sell Stocks")
    drawButton(app.returnButton, "Return")

# Draw a single button with label
def drawButton(rect, label):
    x, y, w, h = rect
    drawRect(x, y, w, h, fill='green', border='darkGreen', borderWidth=2)
    drawLabel(label, x + w//2, y + h//2, size=15, fill='lime', bold=True)

# Mouse click event handler
def stocks_onMousePress(app, mouseX, mouseY):
    if pointInRect(mouseX, mouseY, app.buyButton):
        print('stocksONMOURSEPRES PRESSED')
        setActiveScreen('buyStocks')
    elif pointInRect(mouseX, mouseY, app.sellButton):
        print('stocksONMOURSEPRES PRESSED')
        setActiveScreen('sellStocks')
    elif pointInRect(mouseX, mouseY, app.returnButton):
        app.currDec -= 1
        setActiveScreen('decision')

# Check if point is inside rectangle
def pointInRect(x, y, rect):
    rx, ry, rw, rh = rect
    return (rx <= x <= rx + rw) and (ry <= y <= ry + rh)