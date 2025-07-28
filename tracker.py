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
    drawRect(boxX, boxY, boxWidth, boxHeight, fill='grey')

    # Set padding inside the box
    padding = 20
    lineHeight = 30
    x = boxX + padding
    y = boxY + padding

    # Labels
    drawLabel(f"Player: {app.player.name}", x, y, size=15, align='left')
    drawLabel(f"Savings: ${app.player.money}", x, y + lineHeight, size=15, align='left')
    drawLabel(f"Goal: ${app.player.moneyGoals}", x, y + 2 * lineHeight, size=15, align='left')
    drawLabel(f"Your Stats:", x, 140, size=15, align='left', bold = True)

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
    drawRect(barX, barY, barWidth, barHeight, fill='pink', border='black', align='left')
    drawRect(barX, barY, barWidth * percent, barHeight, fill='green', align = 'left', border = 'black')

    # Label below bar
    drawLabel(f"{int(percent * 100)}% Made", barX, barY + barHeight + 20, align='left', size=15, bold = True)
    drawLabel(f"${app.player.money} / ${app.player.moneyGoals}", barX, barY + barHeight + 40, align='left', size=15)
    # Label for money left to go
    moneyLeftToGo = app.player.moneyGoals - app.player.money
    moneyMsg = abs(moneyLeftToGo)

    labelY = barY + barHeight + 60

    if moneyLeftToGo < 0:
        # Goal exceeded
        drawLabel(f"+${moneyMsg}", barX, labelY,
                fill='green', align='left', size=15)
    elif moneyLeftToGo == 0:
        # Goal achieved
        drawLabel(f"Goal Achieved!", barX, labelY,
                fill='yellow', align='left', size=15)
    else:
        # Still working toward goal
        drawLabel(f"-${moneyMsg}", barX, labelY,
                fill='red', align='left', size=15)

def drawStepsLeft(app):
    stepsLeft = app.time - app.currDec
    color = 'red' if stepsLeft == 0 else 'black'
    drawLabel(f"Steps Left: {stepsLeft} ", app.left + app.border, app.top + 100, 
              size=15, align = 'left', fill=color)


def drawActivityLog(app):
    distFromTracker = 300
    drawLabel("Your Choices:", app.left + app.border, app.top + distFromTracker, size=15, align='left', bold=True)
    for i in range(len(app.log)):
        entry = app.log[i]
        drawLabel(f"{entry}", app.left + app.border, app.top + distFromTracker + (i + 1) * 20, size=15, align='left')