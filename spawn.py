import sys
from cmu_graphics import *

#---Spawn Screen--------------------------------------------------------------------------------------
def spawn_onScreenActivate(app):
    app.name = ''  # Initialize name as an empty string
    pass 

def spawn_redrawAll(app):
    drawLabel("Spawning Screen", app.width/2, app.height/2, size=40, bold=True)
    drawLabel("Enter your name:", app.width/2, app.height/2 - 50)
    drawLabel(app.name, app.width/2, app.height/2 + 50, size=30)
    drawLabel("Press 'Enter' to Continue", app.width/2, app.height/2 + 100)

def spawn_onKeyPress(app, key):
    if key == 'enter':
        setActiveScreen('info')
    elif key == 'backspace':
        if len(app.name) > 0:
            app.name = app.name[:-1]
    elif key.isalpha() and key != 'space':
        app.name += str(key)
    pass  # Ignore other keys