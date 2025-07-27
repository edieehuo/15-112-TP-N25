#--- Baby 2 Billionaire --------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#.....................................................................................................
#--- IMPORTS--------------------------------------------------------------------------------------
import sys
from cmu_graphics import *
from player import *
from playerPortfolio import *
from spawn import *
from info import *
from decision import *

#HAMSTER IMPORTS 
from hamster import *
from run import *

#GAMBLING IMPORTS
from gambling import *
from numbersGame import *
from lottery import * 

#INVESTMENT IMPORTS
from investment import *
from stocks import *
from playerPortfolio import *
from buyStocks import *
from sellStocks import *
from deposits import *

#OTHER
from tracker import *
from end import *

#-----------------------------------------------------------------------------------------------------
#.....................................................................................................
#---Start Screen--------------------------------------------------------------------------------------

def start_onScreenActivate(app):
    #app set up
    app.width = 1000 
    app.height = 1000   
    app.border = 20
    app.screenName = 'start'

    #player set up 
    app.name= ''
    app.money = 0
    app.moneyGoals = 0
    app.time = 0
    app.player = Player(app.name, app.money, app.moneyGoals, app.time)
    app.log = []  # Initialize the activity log
    print(app.player) 

    #player investment 
    app.playerPortfolio = Portfolio(None, None, None)

    #tracking number of decisions made 
    app.currDec = 0    


def start_redrawAll(app):
    drawLabel("Baby 2 Billionaire", app.width/2, app.height/2, size=40, bold=True)
    drawLabel("Press any key to start", app.width/2, app.height/2 + 50)

def start_onKeyPress(app, key):
    setActiveScreen('spawn')


#---Don't Touch Things Below This ---------------------------------------------------------------------------
#............................................................................................................
#--- LIKE REALLY DON'T TOUCH THIS PART ----------------------------------------------------------------------

def main():
    runAppWithScreens(initialScreen='start')
main()

