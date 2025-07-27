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
        drawLabel(f"Stock Price: ${app.stockInfo.stockPrice}", boxX + 5, boxY + padding, size=15, align = 'left')
        drawLabel(f"Stock Volatility: {app.stockInfo.stockVolatility}%", boxX + 5, boxY + padding + lineHeight, size=15, align = 'left')
        drawLabel(f"Key S To Hide Stock Info", boxX + 5, boxY + padding + 2 * lineHeight, size=15, align = 'left', bold = True, fill = 'blue')
    if not app.drawStockInfo:
        drawLabel(f"Key S To Show Stock Info", boxX + 5, boxY + padding + 2 * lineHeight, size=15, align = 'left',  bold = True, fill = 'blue')


