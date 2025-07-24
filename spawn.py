from cmu_graphics import *

#---Spawn Screen--------------------------------------------------------------------------------------
def spawn_onScreenActivate(app):
    pass 

def spawn_redrawAll(app):
    drawLabel("Choose Your Path", app.width/2, 200, size=40, bold=True)
    drawLabel("Press S to start Game", app.width/2, 300)

def spawn_onKeyPress(app, key):
    if key == 's':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys