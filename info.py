import sys
from cmu_graphics import *

#---Information Screen--------------------------------------------------------------------------------------
def info_onScreenActivate(app):
    pass

def info_redrawAll(app):
    drawLabel("Information Screen", app.width/2, 20, size=40, bold=True)
    drawLabel("Welcome to the Game!", app.width/2, 30)
    drawLabel("Choose carefully- no backsies on each step", app.width/2, 50)
    drawLabel("You will be making decisions to reach your money goals", app.width/2, 70)
    drawLabel("You can gamble, invest, or work a job at any given step", app.width/2, 90)

    #Telling player about what they spawned in as
    drawLabel(f"Welcome to adulting, {app.player.name}.", app.width/2, app.height/2 - 20, size = 30, bold=True)
    drawLabel(f"Your Current Bank Account: ${app.player.money},000", app.width/2, app.height/2 + 10)
    drawLabel(f"Your Target Amount To Make: ${app.player.moneyGoals},000", app.width/2, app.height/2 + 40)
    drawLabel(f"Number of Years You Have: {app.player.time}", app.width/2, app.height/2 + 70)

    drawLabel("Hit 'Enter' to Begin Your Journey", app.width/2, app.height/2 + 90, size = 20, bold=True)
    pass

def info_onKeyPress(app, key):
    if key == 'enter':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys