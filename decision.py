#---Decision Screen--------------------------------------------------------------------------------------
import sys
from cmu_graphics import *

def decision_onScreenActivate(app):
    pass

def decision_redrawAll(app):
    drawLabel("Next Choice To Make", app.width/2, 200, size=40, bold=True)
    drawLabel("Press H for Hamster Wheel", app.width/2, 300)
    drawLabel("Press G for Gambling", app.width/2, 350)
    drawLabel("Press I for Investment", app.width/2, 400)

def decision_onKeyPress(app, key):
    if key == 'h':
        setActiveScreen('hamster')
    elif key == 'g':
        setActiveScreen('gambling')
    elif key == 'i':
        setActiveScreen('investment')
    else:
        pass # Ignore other keys
