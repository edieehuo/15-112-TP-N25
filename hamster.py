import sys
from cmu_graphics import *


#---Hamster Wheel Screen--------------------------------------------------------------------------------------
#INCORPORATE INFO ABOUT HAMSTER WHEEL AND HOW TO PLAY HAMSTER WHEEL 

def hamster_onScreenActivate(app):
    app.screenName = 'hamster'
    app.hamsterMoneyAdd = 2
    pass 

def hamster_redrawAll(app):
    drawLabel("Hamster Screen", app.width/2, 10, size=40, bold=True)
    drawLabel("Press R to Run", app.width/2, app.height/2)

def hamster_onKeyPress(app, key):
    if key == 'r':
        setActiveScreen('run')
    else:
        pass  # Ignore other keys

