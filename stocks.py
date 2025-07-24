from cmu_graphics import *
#--- Stocks Screen --------------------------------------------------------------------------------------
def stocks_onScreenActivate(app):
    pass

def stocks_redrawAll(app):
    drawLabel("Stocks Market", app.width/2, 200, size=40, bold=True)
    drawLabel("Press B to Buy Stocks", app.width/2, app.height/2 - 50)
    drawLabel("Press S to Sell Stocks", app.width/2, app.height/2)

def stocks_onKeyPress(app, key):
    if key == 'b':
        pass 
    elif key == 's':
        pass
    elif key == 'space':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys