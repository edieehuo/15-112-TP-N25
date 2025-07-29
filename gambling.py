import sys
from cmu_graphics import *

def gambling_onScreenActivate(app):
    pass
def gambling_redrawAll(app):
    drawLabel("Gambling Screen", app.width/2, 10, size=40, bold=True)
    drawLabel("Press L for Lottery", app.width/2, app.height/2 + 50)

def gambling_onKeyPress(app, key):
    if key == 'l':
        setActiveScreen('lottery')
    else:
        pass  # Ignore other keys