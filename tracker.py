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
    drawRect(boxX, boxY, boxWidth, boxHeight, fill='grey', border='black')

    # Set padding inside the box
    padding = 20
    lineHeight = 30
    x = boxX + padding
    y = boxY + padding

    # Labels
    drawLabel(f"Player: {app.player.name}", x, y, size=15, align='left')
    drawLabel(f"Savings: ${app.player.money},000", x, y + lineHeight, size=15, align='left')
    drawLabel(f"Goal: ${app.player.moneyGoals},000", x, y + 2 * lineHeight, size=15, align='left')

    #Steps Left 
    drawStepsLeft(app)

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
    drawRect(barX, barY, barWidth, barHeight, fill=None, border='black', align='left')
    drawRect(barX, barY, barWidth * percent, barHeight, fill='green', align = 'left', border = 'black')

    # Label below bar
    drawLabel(f"{int(percent * 100)}% Made", barX, barY + barHeight + 20, align='left', size=15, bold = True)
    drawLabel(f"${app.player.money},000 / ${app.player.moneyGoals},000", barX, barY + barHeight + 40, align='left', size=15)
    # Label for money left to go
    moneyLeftToGo = app.player.moneyGoals - app.player.money
    moneyMsg = abs(moneyLeftToGo)

    labelY = barY + barHeight + 60

    if moneyLeftToGo < 0:
        # Goal exceeded
        drawLabel(f"+${moneyMsg},000", barX, labelY,
                fill='green', align='left', size=15)
    elif moneyLeftToGo == 0:
        # Goal achieved
        drawLabel(f"Goal Achieved!", barX, labelY,
                fill='yellow', align='left', size=15)
    else:
        # Still working toward goal
        drawLabel(f"-${moneyMsg},000", barX, labelY,
                fill='red', align='left', size=15)

def drawStepsLeft(app):
    stepsLeft = app.time - app.currDec
    color = 'red' if stepsLeft == 0 else 'black'
    drawLabel(f"Steps Left: {stepsLeft} ", app.left + app.border, app.top + 100, 
              size=15, align = 'left', fill=color)



#----------- ACTIVITY LOG CODE TO WORK ON ---------------------------------------

def drawActivityLog(app):
    drawLabel("Activity Log:", app.left + app.border, app.top + 280, size=15, align='left', bold=True)
    print(app.log)  # Debug: print log to console
    for i, entry in enumerate(app.log):
        drawLabel(f"{entry}", app.left + app.border, app.top + 300 + i * 20, size=15, align='left')
