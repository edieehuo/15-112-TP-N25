import sys
from cmu_graphics import *
#---Running On Hamster Wheel Screen--------------------------------------------------------------------------------------
def run_onScreenActivate(app):
    app.stepsPerSecond = 1
    app.isPaused = False
    pass

def run_redrawAll(app):
    drawLabel("Running On Hamster Wheel", app.width/2, 10, size=40, bold=True)
    drawLabel("Press Space to Return To Decisions", app.width/2, app.height/2)

def run_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys