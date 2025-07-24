import sys
from cmu_graphics import *

#---Numbers Game Screen--------------------------------------------------------------------------------------
def numbersGame_onScreenActivate(app):
    pass

def numbersGame_redrawAll(app):
    drawLabel("Numbers Game", app.width/2, 200, size=40, bold=True)
    drawLabel("Press 1 to Guess a Number", app.width/2, app.height/2 - 50)
    drawLabel("Press 2 to Check Your Guess", app.width/2, app.height/2)

def numbersGame_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('decision')
    else:
        pass
        # Ignore other keys
    