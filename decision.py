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
    app.lowMarketCond = -15
    app.highMarketCond = 15
    app.marketCond = random.randint(app.lowMarketCond,app.highMarketCond)
    updatePortfolioPrices(app)
    #To draw line graph 
    if len(app.marketCondHistory) == app.time: 
        app.marketCondHistory.pop(0)

    app.marketCondHistory.append(app.marketCond)

    buttonW, buttonH = 160, 30
    buttonX = app.width//2 - buttonW//2
    buttonY = 230  # just below the market graph

    app.showStockButton = (buttonX, buttonY, buttonW, buttonH)
    pass

def decision_redrawAll(app):   
    #draw bg 
    drawRect(0,0, app.width, app.height, fill = 'black')
    #DEVELOPMENT NOTE 
    # drawLabel("Decision Screen", app.width/2, 10, size=40, bold=True)
    
    #DRAWING TRACKER 
    tracker_redrawAll(app)  
    investmentTracker_redrawAll(app)  
    
    drawSmallButton(app.showStockButton, "Show New Stock Info")

    if app.drawStockInfo:
        drawNewStockAvail(app)

    #MARKET PLOT 
    playerHoldingTracker_redrawAll(app)

    #DRAWING INFORMATION 
    drawLabel(f" What will you do this month? ", app.width/2, app.height/2-80, 
              fill = 'lime', size=30, bold=True)
    drawBoxes(app)

def drawSmallButton(rect, label):
    x, y, w, h = rect
    drawRect(x, y, w, h, fill='darkGreen', border='darkGrey', borderWidth=2, dashes = True)
    drawLabel(label, x + w//2, y + h//2, size=12, fill='lime', bold=True)

def drawBoxes(app):
    # Draw three boxes 
    boxWidth = 150
    boxHeight = 50
    # Box 1: Hamster Wheel
    drawRect(app.width/2 - boxWidth - 10, app.height/2, boxWidth, boxHeight, fill='red', border='darkRed', borderWidth = 3,  dashes = (10, 5))
    drawLabel("Work", app.width/2 - boxWidth - 10 + boxWidth/2, app.height/2 + boxHeight/2, size=20, bold=True)
    # Box 2: Gambling
    drawRect(app.width/2 + 10, app.height/2, boxWidth, boxHeight, fill='orange', border='chocolate', borderWidth = 3,  dashes = (10, 5))
    drawLabel("Gamble", app.width/2 + 10 + boxWidth/2, app.height/2 + boxHeight/2, size=20, bold=True)
    # Box 3: Investment
    drawRect(app.width/2 - boxWidth/2, app.height/2 + 60, boxWidth, boxHeight, fill='green', border='darkGreen', borderWidth = 3,  dashes = (10, 5))
    drawLabel("Invest", app.width/2 - boxWidth/2 + boxWidth/2, app.height/2 + 60 + boxHeight/2, size=20, bold=True)

def decision_onMousePress(app, mouseX, mouseY):
    if app.time - app.currDec == 0:
        setActiveScreen('end') # If time runs out, go to end screen
        return #this doesn't let u keep on going 

    # Check if the mouse click is within the bounds of any box and set active 
    boxWidth = 150
    boxHeight = 50

    if pointInRect(mouseX, mouseY, app.showStockButton):
        app.drawStockInfo = not app.drawStockInfo
        return
    
    # Box 1: Hamster Wheel
    if (app.width/2 - boxWidth - 10 <= mouseX <= app.width/2 - 10) and (app.height/2 <= mouseY <= app.height/2 + boxHeight):
        app.currDec += 1
        setActiveScreen('hamster')
        return
    # Box 2: Gambling
    elif (app.width/2 + 10 <= mouseX <= app.width/2 + 10 + boxWidth) and (app.height/2 <= mouseY <= app.height/2 + boxHeight):
        app.currDec += 1
        setActiveScreen('lottery')
        return
    # Box 3: Investment
    elif (app.width/2 - boxWidth/2 <= mouseX <= app.width/2 - boxWidth/2 + boxWidth) and (app.height/2 + 60 <= mouseY <= app.height/2 + 60 + boxHeight):
        app.currDec += 1
        setActiveScreen('stocks')
        return

def pointInRect(x, y, rect):
    rx, ry, rw, rh = rect
    return (rx <= x <= rx + rw) and (ry <= y <= ry + rh)

def decision_onKeyPress(app,key): 
    if key == 's':
        app.drawStockInfo = not app.drawStockInfo 

#i am so proud of this... so obvious after i figured it out but this was HARD 😭 ( i can add emojis to code??? heck yeah)
def updatePortfolioPrices(app):
    if app.playerPortfolio.numDiffStocks == 0: pass 
    # print(app.playerPortfolio.stocks)
    for stock in app.playerPortfolio.stocks:
        price, vol = stock
        newPrice =  math.ceil(price*(1+((app.marketCond/100)*vol)))
        numHeld =  app.playerPortfolio.stocks[(price,vol)]['numHeld'] 
        app.playerPortfolio.stocks[(price,vol)]['newValue'] = newPrice * numHeld