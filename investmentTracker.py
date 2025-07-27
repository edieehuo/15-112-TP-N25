import sys
from cmu_graphics import *
from stocks import *
#---Investment Tracker--------------------------------------------------------------------------------------

def investmentTracker_onScreenActivate(app):
    app.drawStockInfo = True

def investmentTracker_redrawAll(app):
    # Background box for the log (move to the right side)
    boxX = app.width - 200  # Move to the right side
    boxY = 0
    boxWidth = 200
    boxHeight = app.height
    drawRect(boxX, boxY, boxWidth, boxHeight, fill='grey', border='black')

    # Set padding inside the box
    padding = 20
    lineHeight = 30
    x = boxX + padding
    y = boxY + padding

    # Draw Stock Info 
    if app.drawStockInfo:
        drawLabel(f"Stock Price: ${app.stockInfo.stockPrice}", boxX, boxY + padding, size=20)
        drawLabel(f"Stock Volatility: {app.stockInfo.stockPercentVolatility}%", boxX, boxY + padding + lineHeight, size=20)
        drawLabel(f"Press S To Hide Stock Market Info", boxX, boxY + padding + 2 * lineHeight, size=20)
    if not app.drawStockInfo:
        drawLabel(f"Press S To See Stock Market Info", boxX, boxY + padding + 2 * lineHeight, size=20)

