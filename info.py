import sys
from cmu_graphics import *

#---Information Screen--------------------------------------------------------------------------------------
def info_onScreenActivate(app):
    pass

def info_redrawAll(app):
    drawLabel("Information Screen", app.width/2, 20, size=40, bold=True)
    drawLabel("Welcome to the Game!", app.width/2, app.height/2 - 50)
    
    #Telling player about what they spawned in as 
    drawLabel(f"Player Name: {app.player.name}", app.width/2, app.height/2 - 20)
    drawLabel(f"Your Current Bank Account: ${app.player.money},000", app.width/2, app.height/2 + 10)
    drawLabel(f"Your Target Amount To Make: ${app.player.moneyGoal},000", app.width/2, app.height/2 + 40)
    drawLabel(f"Number of Years You Have: {app.player.time}", app.width/2, app.height/2 + 70)

    drawLabel("Press 'Enter' to Play", app.width/2, app.height/2 + 90)
    pass

def info_onKeyPress(app, key):
    if key == 'enter':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys