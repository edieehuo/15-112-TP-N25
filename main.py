#--- Baby 2 Billionaire --------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#.....................................................................................................
#--- IMPORTS--------------------------------------------------------------------------------------
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
from lottery import * 

#INVESTMENT IMPORTS
from investment import *
from stocks import *
from playerHoldingTracker import *
from playerPortfolio import *
from buyStocks import *
from sellStocks import *

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

    #player stocks 
    app.playerPortfolio = Portfolio(None, None, None)
    app.invested = 0 

    app.sellStockNum = None 
    app.sellAmount = 0

    app.marketCondHistory = []

    

    #tracking number of decisions made 
    app.currDec = 0    


def start_redrawAll(app):
    # background 
    drawRect(0,0, app.width, app.height, fill = 'black')

    #fonts
    drawLabel("Baby 2 Billionaire", 
              app.width/2, app.height/2, 
              size=100, bold=True, fill = 'forestGreen')

# Draw the Start Game button
    drawButton(app)

# Button to transition to spawn screen
def drawButton(app):
    buttonWidth = 200
    buttonHeight = 50
    buttonX = app.width / 2 - buttonWidth / 2
    buttonY = app.height / 2 + 80 # Position it below the game title

    # Draw button
    drawRect(buttonX, buttonY, buttonWidth, buttonHeight, fill='forestGreen', border='green')
    drawLabel("Start Game", buttonX + buttonWidth / 2, buttonY + buttonHeight / 2, size=24, bold=True, fill='lime')

# Detect mouse click on the Start Game button
def start_onMousePress(app, mouseX, mouseY):
    buttonWidth = 200
    buttonHeight = 50
    buttonX = app.width / 2 - buttonWidth / 2
    buttonY = app.height / 2 + 80 # Position it below the game title

    # Check if the mouse click is inside the button
    if buttonX <= mouseX <= buttonX + buttonWidth and buttonY <= mouseY <= buttonY + buttonHeight:
        setActiveScreen('spawn')  # Transition to the spawn screen


#---Don't Touch Things Below This ---------------------------------------------------------------------------
#............................................................................................................
#--- LIKE REALLY DON'T TOUCH THIS PART ----------------------------------------------------------------------

def main():
    runAppWithScreens(initialScreen='start')
main()

