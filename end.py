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

    drawLabel(f"You made a total of ${app.player.money},000.", app.width/2, app.height/2 + 10)
    drawLabel("Press 'Enter' to restart", app.width/2, app.height/2 + 70)

def end_onKeyPress(app, key):
    if key == 'enter':
        setActiveScreen('start')  # Restart the game
    else:
        pass  # Ignore other keys