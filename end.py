import sys
from cmu_graphics import *

#---End Screen--------------------------------------------------------------------------------------
def end_onScreenActivate(app):
    pass

def end_redrawAll(app):
    drawLabel("End Screen", app.width/2, 10, size=40, bold=True)
    
    if app.player.money >= app.player.moneyGoals:
        drawLabel(f"You reached your goal of ${app.player.moneyGoals},000!", app.width/2, app.height/2 - 20)
    else:
        drawLabel(f"You did not reach your goal of ${app.player.moneyGoals},000.", app.width/2, app.height/2 - 20)
        barX = 150
        barY = 100
        barWidth = 500
        barHeight = 30
        percent = app.player.money / app.player.moneyGoals
        percent = min(max(percent, 0), 1)
        drawRect(barX, barY, barWidth, barHeight, fill='red', border='black')
        drawRect(barX, barY, barWidth * percent, barHeight, fill='lightGreen', border ='black')
        drawLabel(f"${app.player.money},000 / ${app.player.moneyGoals},000", app.width/2, barY + barHeight + 15)
    pass 

    drawLabel(f"You made a total of ${app.player.money},000.", app.width/2, app.height/2 + 10)
    drawLabel("Press 'Enter' to restart", app.width/2, app.height/2 + 70, bold=True)

def end_onKeyPress(app, key):
    if key == 'enter':
        setActiveScreen('start')  # Restart the game
    else:
        pass  # Ignore other keys