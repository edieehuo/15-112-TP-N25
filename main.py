from cmu_graphics import *
from welcomeScreen import *

def onAppStart(app):
    app.mode = 'welcome'  # Initial mode
    app.width = 800
    app.height = 600
    app.player = None  # Placeholder for player object
    app.score = 0  # Initialize score for the game
    app.gameOver = False  # Flag to check if the game is over

def redrawAll(app):
    if app.mode == 'welcome':
        drawWelcomeScreen(app)
    elif app.mode == 'game':
        drawGameScreen(app)
    elif app.mode == 'gameOver':
        drawGameOverScreen(app)
    else:
        pass

def resetApp(app):
    app.mode = 'welcome'
    app.player = None
    app.score = 0
    app.gameOver = False

#---Event Handlers-----------------------------------------------------------------------------------
def onKeyPress(app, key):
    if app.mode == 'game':
        if key == 'r':  # Restart game
            app.mode = 'game'
        elif key == 'q':  # Quit game
            app.mode = 'welcome'


#---Drawing Functions--------------------------------------------------------------------------------
def drawWelcomeScreen(app):
    pass 

def drawGameScreen(app):
    pass

def drawGameOverScreen(app):
    pass 

#---Don't Touch--------------------------------------------------------------------------------------
def main():
    runApp()
main()
