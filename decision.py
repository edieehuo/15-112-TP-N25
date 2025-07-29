import math
#IMPORTS=================================================================================================
from cmu_graphics import *
from tracker import *  
from investmentTracker import *
from playerHoldingTracker import *
from stocks import *
#-----------------------------------------------------------------------------------------------------
#---Decision Screen--------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
import random
def decision_onScreenActivate(app):
    app.screenName = 'decision'
    #STOCKS SET UP
    app.drawStockInfo = False
    app.stockPrice = random.randint(100, 1000)
    app.stockVolatility = random.randint(10, 20)
    app.stockInfo = stockInfo(app.stockPrice, app.stockVolatility)

    #market condition random generation that uniformly affects newValue of EVERY stock
    #initializes without this app.marketCond when buyer just buys something
    app.lowMarketCond = -10
    app.highMarketCond = 25
    app.marketCond = random.randint(app.lowMarketCond,app.highMarketCond)
    updatePortfolioPrices(app)

    #To draw line graph 
    app.marketCondHistory.append(app.marketCond)

    
    pass

#i am so proud of this... so obvious after i figured it out but this was HARD 😭 ( i can add emojis to code??? heck yeah)
def updatePortfolioPrices(app):
    if app.playerPortfolio.numDiffStocks == 0: pass 
    # print(app.playerPortfolio.stocks)
    for stock in app.playerPortfolio.stocks:
        price, vol = stock
        newPrice =  math.ceil(price*(1+((app.marketCond/100)*vol)))
        numHeld =  app.playerPortfolio.stocks[(price,vol)]['numHeld'] 
        app.playerPortfolio.stocks[(price,vol)]['newValue'] = newPrice * numHeld



def decision_redrawAll(app):   
    #DEVELOPMENT NOTE 
    drawLabel("Decision Screen", app.width/2, 10, size=40, bold=True)

    #DRAWING TRACKER 
    tracker_redrawAll(app)  
    investmentTracker_redrawAll(app)  
    playerHoldingTracker_redrawAll(app)

    #DRAWING INFORMATION 
    drawLabel(f" Choose Carefully...  ", app.width/2, app.height/2-80, size=40, bold=True)

    drawLabel("Press H for Hamster Wheel", app.width/2, app.height/2)
    drawLabel("Press G for Gambling", app.width/2, app.height/2 + 25)
    drawLabel("Press I for Investment", app.width/2, app.height/2 + 50)

def decision_onKeyPress(app, key): 
    if app.currDec == app.time:
        setActiveScreen('end') # If time runs out, go to end screen
        return #this doesn't let u keep on going 
    if key == 's':
        app.drawStockInfo = not app.drawStockInfo  # Toggle stock info display

    if key == 'h':
        app.currDec += 1
        setActiveScreen('hamster')
        return 
    elif key == 'g':
        app.currDec += 1
        setActiveScreen('gambling')
        return 
    elif key == 'i':
        app.currDec += 1
        setActiveScreen('investment')
        return 
    else:
        pass # Ignore other keys
