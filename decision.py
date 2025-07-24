import sys
from cmu_graphics import *

#---Decision Screen--------------------------------------------------------------------------------------
def decision_onScreenActivate(app):
    pass

def decision_redrawAll(app):
    drawLabel(f" Time For {app.name} To Make A Choice...  ", app.width/2, app.height/2-100, size=40, bold=True)
    drawLabel("Press H for Hamster Wheel", app.width/2, app.height/2 - 50)
    drawLabel("Press G for Gambling", app.width/2, app.height/2)
    drawLabel("Press I for Investment", app.width/2, app.height/2 + 50)

def decision_onKeyPress(app, key):
    app.currDec += 1  # Decrease time by 1 for each decision made
    print(f'{app.currDec}, {app.time}')  # Debug: check time remaining
    if app.currDec == app.time:
        setActiveScreen('end') # If time runs out, go to end screen
        return #this doesn't let u keep on going 
    
    if key == 'h':
        setActiveScreen('hamster')
    elif key == 'g':
        setActiveScreen('gambling')
    elif key == 'i':
        setActiveScreen('investment')
    if key == 'left':
        pass
    else:
        pass # Ignore other keys
