import sys
#IMPORTS=================================================================================================
from cmu_graphics import *
from tracker import *  
from investmentTracker import *
from stocks import *
#-----------------------------------------------------------------------------------------------------
#---Decision Screen--------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
import random
def decision_onScreenActivate(app):
    app.screenName = 'decision'
    print('decision screen app.playerPortfolio', {app.playerPortfolio})
    #STOCKS SET UP
    app.drawStockInfo = False
    app.stockPrice = random.randint(100, 1000)
    app.stockVolatility = random.randint(10, 20)
    app.stockInfo = stockInfo(app.stockPrice, app.stockVolatility)

    pass

def decision_redrawAll(app):   
    #DEVELOPMENT NOTE 
    drawLabel("Decision Screen", app.width/2, 10, size=40, bold=True)

    #DRAWING TRACKER 
    tracker_redrawAll(app)  # Assuming tracker_redrawAll is defined elsewhere
    investmentTracker_redrawAll(app)  # Assuming investmentTracker_redrawAll is defined elsewhere

    #DRAWING INFORMATION 
    drawLabel(f" Choose Carefully...  ", app.width/2, app.height/2-100, size=40, bold=True)
    drawLabel("Press H for Hamster Wheel", app.width/2, app.height/2 - 50)
    drawLabel("Press G for Gambling", app.width/2, app.height/2)
    drawLabel("Press I for Investment", app.width/2, app.height/2 + 50)

def decision_onKeyPress(app, key): 
    if app.currDec == app.time:
        setActiveScreen('end') # If time runs out, go to end screen
        return #this doesn't let u keep on going 
    if key == 's':
        app.drawStockInfo = not app.drawStockInfo  # Toggle stock info display

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
        setActiveScreen('investment')
        return 
    else:
        pass # Ignore other keys
