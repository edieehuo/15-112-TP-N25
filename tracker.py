import sys
from cmu_graphics import *
#--- Tracker Screen --------------------------------------------------------------------------------------
'''Draw on every screen while game is active to show player info, time left, and money.'''
def tracker_redrawAll(app):

    # Background box for the log
    boxX = 0
    boxY = 0
    boxWidth = 200
    boxHeight = app.height
    drawRect(boxX, boxY, boxWidth, boxHeight, fill='black')

    # Set padding inside the box
    padding = 20
    lineHeight = 30
    x = boxX + padding
    y = boxY + padding

    charWidth = 13
    # Labels
    drawLabel(f"Player:", 
              x, y, 
              fill = 'lime', size=20, align='left', bold = True)
    drawLabel(f"{app.player.name}", 
              x+len('Player:')*charWidth, y, 
              fill = 'white', size=15, align='left', font = 'monospace', bold= True )
    drawLabel(f"Savings:" , 
              x, y + lineHeight, 
              fill = 'lime', size=20, align='left', bold = True)
    drawLabel(f"${app.player.money}", 
              x+len('Savings:')*charWidth, y + lineHeight,
              fill = 'white', size=15, align='left', font = 'monospace', bold= True )
    drawLabel(f"Goal:" , 
              x, y + 2*lineHeight, 
              fill = 'lime', size=20, align='left', bold = True)
    drawLabel(f"${app.player.moneyGoals}", 
              x+len('Goal:')*charWidth, y + 2*lineHeight,
              fill = 'white', size=15, align='left', font = 'monospace', bold= True )

    #draw Steps Left 
    stepsLeft = app.time - app.currDec
    color = 'red' if stepsLeft < 3 else 'white'

    drawLabel(f"Months Left: {stepsLeft}", x, y + 3*lineHeight, 
              size=20, bold = True, align = 'left', fill= 'lime')
    
    drawLabel(f"Progress:", 
              x, y + 4*lineHeight, 
              fill = 'lime',size=20, align='left', bold = True)

    # Percentage bar
    drawPercentage(app, x, y + 5 * lineHeight)

    # Draw activity log
    drawActivityLog(app)

def drawPercentage(app, barX, barY):
    barWidth = 150
    barHeight = 20
    percent = app.player.money / app.player.moneyGoals
    percent = min(max(percent, 0), 1)

    # Progress bar
    drawRect(barX, barY, barWidth, barHeight, fill='pink', border='black', align='left')
    if percent > 0:
        drawRect(barX, barY, barWidth * percent, barHeight, fill='green', align = 'left', border = 'black')

    # Label below bar
    drawLabel(f"{int(percent * 100)}% Made", 
              barX, barY + barHeight + 20, 
              fill = 'white', align='left', size=15, bold = True)
    drawLabel(f"${app.player.money} / ${app.player.moneyGoals}", barX, barY + barHeight + 40, 
              fill = 'white', align='left', size=15)
    
    # Label for money left to go
    moneyLeftToGo = app.player.moneyGoals - app.player.money
    moneyMsg = abs(moneyLeftToGo)

    labelY = barY + barHeight + 60
    if moneyLeftToGo < 0:
        # Goal exceeded
        drawLabel(f"+${moneyMsg}", barX, labelY,
                fill='lime', align='left', size=15)
    elif moneyLeftToGo == 0:
        # Goal achieved
        drawLabel(f"Goal Achieved!", barX, labelY,
                fill='yellow', align='left', size=15)
    else:
        # Still working toward goal
        drawLabel(f"-${moneyMsg}", barX, labelY,
                fill='red', align='left', size=15)

def drawActivityLog(app):
    distFromTracker = 300
    drawLabel("Transaction Log:", app.left + app.border, app.top + distFromTracker, 
              fill = 'lime', size=20, align='left', bold=True)
    for i in range(len(app.log)):
        entry = app.log[i]
        drawLabel(f"{entry}", app.left + app.border, app.top + distFromTracker + (i + 1) * 20, 
                  fill = 'white', size=15, align='left')