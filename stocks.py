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

def drawMarketPlot(app, boxX, boxY, boxWidth, boxHeight):
    # print('playerHldingTrcker: drawMarketPlot: app.marketCondHistory:', app.marketCondHistory)
    minCond = app.lowMarketCond
    maxCond = app.highMarketCond

    dataPoints = len(app.marketCondHistory)
    
    if dataPoints == 1:
        pass 
    else:
        drawLabel(f"Current Market Condition", app.width/2, 55, 
              fill = 'lime', bold = True, size = 20)
        labelX = app.width//2
        labelY = 80
        if app.marketCond > 0:
            drawLabel(f"{app.marketCond}",
                    labelX, labelY, 
                    size=15, align = 'left', bold = True, fill = 'red')
        if app.marketCond <= 0:
            drawLabel(f"{app.marketCond}",
                    labelX, labelY,
                    size=15, align = 'left', bold = True, fill = 'green')

        # Draw the line plot for multiple data points
        stepInterval = app.time  # Number of fixed intervals
        for i in range(1, dataPoints):
            # Calculate x based on fixed intervals
            x1 = boxX + (i - 1) * (boxWidth / stepInterval)
            y1 = boxY + boxHeight - ((app.marketCondHistory[i - 1] - minCond) / (maxCond - minCond)) * boxHeight
            x2 = boxX + i * (boxWidth / stepInterval)
            y2 = boxY + boxHeight - ((app.marketCondHistory[i] - minCond) / (maxCond - minCond)) * boxHeight

            # Draw the line between the two points
            drawLine(x1, y1, x2, y2, fill='white')

            drawCircle(x2, y2, 7, fill='darkGrey')  # Circle behind the value
            drawCircle(x2, y2, 5, fill='black')  # Main circle (marker)

            drawLabel(f"{app.marketCondHistory[i]}", x2, y2, size = 10, bold = True, fill='lime')

        # Draw the vertical axis line on the left side
        axisX = boxX  # Position of the axis line (at the left side of the box)
        axisYStart = boxY  # Starting point for the axis (at the bottom of the box)
        axisYEnd = boxY + boxHeight  # Ending point for the axis (at the top of the box)
        drawLine(axisX, axisYStart, axisX, axisYEnd, fill='white', lineWidth=2)
        drawLine(axisX, (boxY+boxHeight//2), axisX + boxWidth, (boxY+boxHeight//2), fill='white', lineWidth=2, dashes= True)
        drawLine(axisX + boxWidth, axisYStart, axisX + boxWidth, axisYEnd, fill='white', lineWidth=2)


def drawPortfolio(app): 
    boxX = 200 # right edge of tracker 
    boxY = 550 #where to stop 

    marketPlotX = boxX
    marketPlotY = boxY
    #variable 
    marketPlotHeight = 100

    holdX = marketPlotX
    holdY = marketPlotY + marketPlotHeight
    # print(app.playerPortfolio)
    # print(app.playerPortfolio.numDiffStocks)
    if app.playerPortfolio.numDiffStocks == 0: 
        pass 
    else: 
        drawLabel(f"Your Holdings:", boxX + 20, 635, 
              fill = 'lime', bold = True, size = 20, align = 'left')
        i = 0
        iToMod = 0
        stockSpacing = 18
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
            distBottomScreen = 40
            if holdY + i*stockSpacing <= app.height - distBottomScreen:
                iToMod += 1
                drawLabel(f"{i}: Buy Price ${buyPrice}", 
                          holdX + stockColPadding, 
                          holdY + i*stockSpacing, align = 'left',  fill = 'lime',
                          size = 15)
                drawLabel(f"Market Price ${sellPrice}", 
                          holdX + stockColPadding + priceToSellPriceSpacing, 
                          holdY + i*stockSpacing, align = 'left', fill = 'white',
                          size = 15)
            else: 
                drawLabel(f"{i}: Buy Price ${buyPrice}", 
                          holdX + stockColPadding*2 + stockColSpacing*3 + priceToSellPriceSpacing*2, 
                          holdY + (i%iToMod)*stockSpacing, 
                          fill = 'lime', align = 'left', 
                          size = 15)
                drawLabel(f"Market Price ${sellPrice}", 
                          holdX + stockColPadding*2 + stockColSpacing*4 + priceToSellPriceSpacing*3, 
                          holdY + (i%iToMod)*stockSpacing, fill = 'white', align = 'left', 
                          size = 15)

    pass 
