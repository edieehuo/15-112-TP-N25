#---Baby 2 Billionaire Game--------------------------------------------------------------------------------------
import sys
from cmu_graphics import *
from spawn import *
from decision import * 
from player import *
from hamster import *
from gambling import *
from investment import *

#---Start Screen--------------------------------------------------------------------------------------
def start_onScreenActivate(app):
    app.width = 800 
    app.height = 600  

def start_redrawAll(app):
    drawLabel("Baby 2 Billionaire", app.width/2, 200, size=40, bold=True)
    drawLabel("Press any key to start", app.width/2, 300)

def start_onKeyPress(app, key):
    setActiveScreen('spawn')

#---Don't Touch--------------------------------------------------------------------------------------
def main():
    runAppWithScreens(initialScreen='start')
main()

