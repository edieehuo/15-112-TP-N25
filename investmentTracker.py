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
    drawRect(boxX, boxY, boxWidth, boxHeight, fill='grey')

    # Set padding inside the box
    padding = 20
    lineHeight = 30

    #Draw Market Conditions 
    # labelX = app.width//2
    # labelY = 80
    # if app.marketCond > 0:
    #     drawLabel(f"{app.marketCond}",
    #             labelX, labelY, 
    #             size=15, align = 'left', bold = True, fill = 'red')
    # if app.marketCond <= 0:
    #     drawLabel(f"{app.marketCond}",
    #             labelX, labelY,
    #             size=15, align = 'left', bold = True, fill = 'green')
    
    # Draw Stock Info 
    drawLabel(f"Stock Avail. To Buy", boxX + 5, boxY + padding + 40, 
              align = 'left', bold = True, fill = 'green', size = 15)
    if app.drawStockInfo:        
        drawLabel(f"Key S To Hide Stock Info", boxX + 5, boxY + padding + 2 * lineHeight, 
                  size=15, align = 'left', bold = True, fill = 'blue')
        drawLabel(f"Stock Price: ${app.stockInfo.stockPrice}", boxX + 10, 100,
                  size=15, align = 'left')
        drawLabel(f"Stock Volatility: {app.stockInfo.stockVolatility}%", boxX + 10, 120,size=15, align = 'left')
    if not app.drawStockInfo:
        drawLabel(f"Key S To Show Stock Info", boxX + 5, boxY + padding + 2 * lineHeight, size=15, align = 'left',  bold = True, fill = 'blue')


