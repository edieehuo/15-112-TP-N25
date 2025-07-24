import sys
from cmu_graphics import *

#---Decision Screen--------------------------------------------------------------------------------------
def decision_onScreenActivate(app):
    pass

def decision_redrawAll(app):
    drawLabel(f"{app.name} Next Choice To Make", app.width/2, app.height/2-100, size=40, bold=True)
    drawLabel("Press H for Hamster Wheel", app.width/2, app.height/2 - 50)
    drawLabel("Press G for Gambling", app.width/2, app.height/2)
    drawLabel("Press I for Investment", app.width/2, app.height/2 + 50)

def decision_onKeyPress(app, key):
    if key == 'h':
        setActiveScreen('hamster')
    elif key == 'g':
        setActiveScreen('gambling')
    elif key == 'i':
        setActiveScreen('investment')
    else:
        pass # Ignore other keys
