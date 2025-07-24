import sys
from cmu_graphics import *

#---Lottery Screen--------------------------------------------------------------------------------------
def lottery_onScreenActivate(app):
    pass

def lottery_redrawAll(app):
    drawLabel("Lottery Screen", app.width/2, 200, size=40, bold=True)
    drawLabel("Press L to Play Lottery", app.width/2, app.height/2 - 50)
    drawLabel("Press R to Return to Gambling Choices", app.width/2, app.height/2)

def lottery_onKeyPress(app, key):
    if key == 'l':
        pass 
    elif key == 'r':
        setActiveScreen('gambling')  # Return to gambling choices
    else:
        pass  # Ignore other keys

