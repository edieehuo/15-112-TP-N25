import sys
from cmu_graphics import *

#---Information Screen--------------------------------------------------------------------------------------
def info_onScreenActivate(app):
    pass

def info_redrawAll(app):
    drawLabel("Information Screen", app.width/2, app.height/2, size=40, bold=True)
    drawLabel("Press 'Enter' to Play", app.width/2, app.height/2 + 50)
    pass

def info_onKeyPress(app, key):
    if key == 'enter':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys