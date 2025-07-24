import sys
from cmu_graphics import *


#---Hamster Wheel Screen--------------------------------------------------------------------------------------
def hamster_onScreenActivate(app):
    pass 

def hamster_redrawAll(app):
    drawLabel("Hamster Wheel", app.width/2, app.height/2 - 100, size=40, bold=True)
    drawLabel("Press R to Run", app.width/2, app.height/2)

def hamster_onKeyPress(app, key):
    if key == 'r':
        setActiveScreen('run')
    else:
        pass  # Ignore other keys

