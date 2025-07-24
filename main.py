#---Baby 2 Billionaire Game--------------------------------------------------------------------------------------
#--- Imports--------------------------------------------------------------------------------------
import sys
from cmu_graphics import *
from player import Player
from spawn import *
from info import *
from decision import *
from hamster import *
from gambling import *
from investment import *


#---Start Screen--------------------------------------------------------------------------------------
def start_onScreenActivate(app):
    #app set up 
    app.width = 800 
    app.height = 600  

    #player set up 
    app.name= ''
    app.money = 0
    app.moneyGoals = 0
    app.time = 0
    app.player = Player(app.name, app.money, app.moneyGoals, app.time)
    print(app.player) 

def start_redrawAll(app):
    drawLabel("Baby 2 Billionaire", app.width/2, app.height/2, size=40, bold=True)
    drawLabel("Press any key to start", app.width/2, app.height/2 + 50)

def start_onKeyPress(app, key):
    setActiveScreen('spawn')


#---Don't Touch This Part -----------------------------------------------------------------------------------
def main():
    runAppWithScreens(initialScreen='start')
main()

