from cmu_graphics import *
from player import *
from playerPortfolio import *
from spawn import *
from info import *
from decision import *

#INVESTMENT IMPORTS
from investment import *
from stocks import *
from playerPortfolio import *
from buyStocks import *
from sellStocks import *

#OTHER
from tracker import *
#--------------------------------------------------------------------------------------------------------------------------------------------

def playerHoldingTracker_redrawAll(app):
    boxX = 200 # right edge of tracker 
    boxY = 700 #where to stop 
    boxWidth = 600 #width from right edge of tracker to left edge of investment 
    boxHeight = app.height - boxY #until bottom

    drawRect(boxX, boxY, boxWidth, boxHeight, fill='grey')
    drawLine(boxX, 0, boxX, app.height, fill = 'white')
    drawLine(boxX + boxWidth, 0, boxX + boxWidth, app.height, fill = 'white')

    marketPlotX = boxX
    marketPlotY = boxY
    marketPlotWidth = boxWidth
    #variable 
    marketPlotHeight = 100
    #draw line plot of market cond variable
    drawMarketPlot(app, marketPlotX, marketPlotY, marketPlotWidth, marketPlotHeight)
    #draw player portoflio 
    drawPortfolio(app)
    pass 

# Helper function to draw market condition plot
def drawMarketPlot(app, boxX, boxY, boxWidth, boxHeight):
    print('playerHldingTrcker: drawMarketPlot: app.marketCondHistory:', app.marketCondHistory)
    minCond = app.lowMarketCond
    maxCond = app.highMarketCond

    dataPoints = len(app.marketCondHistory)
    
    if dataPoints == 1:
        # If there's only one data point, just draw a marker at the position of that point
        stepInterval = app.time  # Number of fixed intervals
        x = boxX + 10 
        y = boxY + boxHeight - ((app.marketCondHistory[0] - minCond) / (maxCond - minCond)) * boxHeight
        
        # Draw a circle (marker) for the single data point
        drawCircle(x, y, 5, fill='white')  # Adjust size of the marker (radius = 5)
        drawLabel(f"{dataPoints}", x, y, fill='white')  # Adjust size of the marker (radius = 5)

        #Draw box around: 
        drawRect(boxX, boxY, boxWidth, boxHeight, fill = None, border = 'black')
    else:
        # Draw the line plot for multiple data points
        stepInterval = app.time  # Number of fixed intervals
        
        for i in range(1, dataPoints):
            # Calculate x based on fixed intervals
            x1 = boxX + (i - 1) * (boxWidth / stepInterval)
            y1 = boxY + boxHeight - ((app.marketCondHistory[i - 1] - minCond) / (maxCond - minCond)) * boxHeight
            x2 = boxX + i * (boxWidth / stepInterval)
            y2 = boxY + boxHeight - ((app.marketCondHistory[i] - minCond) / (maxCond - minCond)) * boxHeight

            #Draw Circle at each point
            drawCircle(x2, y2, 5, fill='white')  # Adjust size of the marker (radius = 5)
            drawLabel(f"{app.marketCondHistory[i]}", x2, y2, fill='black')


            # Draw the line between the two points
            drawLine(x1, y1, x2, y2, fill='black')

            # Draw around plot 
            drawRect(boxX, boxY, boxWidth, boxHeight, fill = None, border = 'black')

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
        for stock in app.playerPortfolio.stocks:
            i += 1
            buyPrice, vol = stock # don't need volatility to be drawn 
            # print('drawPort buy', buyPrice)
            if holdY + i*stockSpacing <= app.height:
                iToMod += 1
                drawLabel(f"{buyPrice}", holdX + stockColPadding, holdY + i*stockSpacing, size = 15)
            else: 
                drawLabel(f"{buyPrice}", holdX + stockColPadding + stockColSpacing, holdY + (i%iToMod)*stockSpacing, size = 15)
    pass 