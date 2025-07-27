from cmu_graphics import *
from player import *
from playerPortfolio import *
from spawn import *
from info import *
from decision import *

#INVESTMENT IMPORTS
from investment import *
from stocks import *
from playerPortfolio import *
from buyStocks import *
from sellStocks import *

#OTHER
from tracker import *
#--------------------------------------------------------------------------------------------------------------------------------------------
def playerHoldingTracker_onScreenActivate(app):
    pass 

def playerHoldingTracker_redrawAll(app):
    boxX = 200 # right edge of tracker 
    boxY = 700 #where to stop 
    boxWidth = 600 #width from right edge of tracker to left edge of investment 
    boxHeight = app.height - boxY #until bottom
    drawRect(boxX, boxY, boxWidth, boxHeight, fill='grey')
    pass 
