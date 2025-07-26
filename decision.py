import sys
from cmu_graphics import *
from tracker import *  

#---Decision Screen--------------------------------------------------------------------------------------
def decision_onScreenActivate(app):
    pass

def decision_redrawAll(app):
    drawLabel("Decision Screen", app.width/2, 10, size=40, bold=True)

    drawLabel(f" Choose Carefully...  ", app.width/2, app.height/2-100, size=40, bold=True)
    tracker_redrawAll(app)  # Assuming tracker_redrawAll is defined elsewhere
    drawLabel("Press H for Hamster Wheel", app.width/2, app.height/2 - 50)
    drawLabel("Press G for Gambling", app.width/2, app.height/2)
    drawLabel("Press I for Investment", app.width/2, app.height/2 + 50)

def decision_onKeyPress(app, key): 
    if app.currDec == app.time:
        setActiveScreen('end') # If time runs out, go to end screen
        return #this doesn't let u keep on going 
    if key == 'h':
        app.currDec += 1
        app.log.insert(0,"+2,000 Hamster Wheel")
        setActiveScreen('hamster')
        return 
    elif key == 'g':
        app.currDec += 1
        app.log.insert(0,"Chose Gambling")
        setActiveScreen('gambling')
        return 
    elif key == 'i':
        app.currDec += 1
        app.log.insert(0,"Chose Investment")
        setActiveScreen('investment')
        return 
    else:
        pass # Ignore other keys
