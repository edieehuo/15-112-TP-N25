import sys
from cmu_graphics import *

def investment_onScreenActivate(app):
    app.screenName = 'investment'
    pass
    
def investment_redrawAll(app):
    drawLabel("Investment Screen", app.width/2, 10, size=40, bold=True)

    drawLabel("Press S for Stocks", app.width/2, app.height/2 - 50)
    drawLabel("Press D for Deposits", app.width/2, app.height/2)

def investment_onKeyPress(app, key):
    if key == 's':
        app.screenName = 'stocks'
        setActiveScreen('stocks')
    elif key == 'd':
        app.screenName = 'deposits'
        setActiveScreen('deposits')
    else:
        pass  # Ignore other keys