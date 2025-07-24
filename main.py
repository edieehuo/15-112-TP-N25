#---Baby 2 Billionaire Game--------------------------------------------------------------------------------------
from cmu_graphics import *
from player import *
from hamster import *
from gambling import *
from investment import *
#importing is not working! 
# print(hamster_redrawAll) 

#---Start Screen--------------------------------------------------------------------------------------
def start_onScreenActivate(app):
    app.gameState = False  # Initialize game state to False
    app.player = None  

def start_redrawAll(app):
    drawLabel("Baby 2 Billionaire", app.width/2, 200, size=40, bold=True)
    drawLabel("Press any key to start", app.width/2, 300)

def start_onKeyPress(app, key):
    setActiveScreen('spawn')

#---Spawn Screen--------------------------------------------------------------------------------------
def spawn_redrawAll(app):
    drawLabel("Choose Your Path", app.width/2, 200, size=40, bold=True)
    player = player(app.name, 0, rand(1000, 10000), rand(10000, 100000)) 
    drawLabel("Press S to start Game", app.width/2, 300)

def spawn_onKeyPress(app, key):
    if key == 's':
        app.gameState = True 
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys

#---Decision Screen--------------------------------------------------------------------------------------

def decision_redrawAll(app):
    drawLabel("Next Choice To Make", app.width/2, 200, size=40, bold=True)
    drawLabel("Press H for Hamster Wheel", app.width/2, 300)
    drawLabel("Press G for Gambling", app.width/2, 350)
    drawLabel("Press I for Investment", app.width/2, 400)

def decision_onKeyPress(app, key):
    if key == 'h':
        setActiveScreen('hamster')
    elif key == 'g':
        setActiveScreen('gambling')
    elif key == 'i':
        setActiveScreen('investment')
    else:
        pass # Ignore other keys

#---Don't Touch--------------------------------------------------------------------------------------
def main():
    runAppWithScreens(initialScreen='start', width=800, height=600)
main()
