import sys
from cmu_graphics import *
#--- Deposits Screen --------------------------------------------------------------------------------------

def deposits_onScreenActivate(app):
    pass

def deposits_redrawAll(app):
    drawLabel("Deposits Screen", app.width/2, 10, size=40, bold=True)

    drawLabel("Deposit Your Money", app.width/2, 200, size=40, bold=True)
    drawLabel("Press A to Add Money", app.width/2, app.height/2 - 50)
    drawLabel("Press R to Remove Money", app.width/2, app.height/2)

def deposits_onKeyPress(app, key):
    if key == 'a':
        pass
    elif key == 'r':
        pass
    elif key == 'space':
        setActiveScreen('decision')  # Go back to decision screen
    else:
        pass  # Ignore other keys