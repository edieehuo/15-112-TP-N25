import sys
from cmu_graphics import *

#---Information Screen--------------------------------------------------------------------------------------
def info_onScreenActivate(app):
    app.drawRules = False 
    pass

def info_redrawAll(app):
    drawLabel("Information Screen, space for Rules", app.width/2, 20, size=40, bold=True)
    if app.drawRules: 
        drawLabel("Choose carefully- no backsies on each step", app.width/2,app.height/2 - 150)
        drawLabel("You will be making decisions to reach your money goals", app.width/2, app.height/2 - 120)
        drawLabel("You can gamble, invest, or work a job at any given step", app.width/2, app.height/2 - 130)

    #Telling player about what they spawned in as
    drawLabel(f"Welcome to adulting, {app.player.name}.", app.width/2, app.height/2 - 20, size = 30, bold=True)
    drawLabel(f"Your Current Bank Account: ${app.player.money}", app.width/2, app.height/2 + 10)
    drawLabel(f"Your Target Amount To Make: ${app.player.moneyGoals}", app.width/2, app.height/2 + 40)
    drawLabel(f"Number of Years You Have: {app.player.time}", app.width/2, app.height/2 + 70)

    drawLabel("Hit 'Enter' to Begin Your Journey", app.width/2, app.height/2 + 90, size = 20, bold=True)
    drawLabel("Hit 'Space' to Read Instructions", app.width/2, app.height/2 + 130, size = 20, bold=True)

    pass

def info_onKeyPress(app, key):
    if key == 'space':
        app.drawRules = not app.drawRules #toggle app.drawRules  

    if key == 'enter':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys