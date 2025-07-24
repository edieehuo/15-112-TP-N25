import sys
from cmu_graphics import *


def investment_onScreenActivate(app):
    pass

def investment_redrawAll(app):
    drawLabel("Investment Opportunities", app.width/2, 200, size=40, bold=True)
    drawLabel("Press S for Stocks", app.width/2, app.height/2 - 50)
    drawLabel("Press D for Deposits", app.width/2, app.height/2)

def investment_onKeyPress(app, key):
    if key == 's':
        setActiveScreen('stocks')
    elif key == 'd':
        setActiveScreen('deposits')
    else:
        pass  # Ignore other keys