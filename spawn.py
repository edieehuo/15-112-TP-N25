import sys
from cmu_graphics import *
import random

#---Spawn Screen--------------------------------------------------------------------------------------
def spawn_onScreenActivate(app):
    app.name = ''  # Initialize name as an empty string
    pass 

def spawn_redrawAll(app):
    drawLabel("Spawning Screen", app.width/2, 10, size=40, bold=True)
    drawLabel("Enter your name:", app.width/2, app.height/2 - 50)
    drawLabel(app.name, app.width/2, app.height/2 + 50, size=30)
    drawLabel("Press 'Enter' to Continue", app.width/2, app.height/2 + 100)

def spawn_onKeyPress(app, key):
    if key == 'enter':
        # Generate goalmoney, starting money, number of "years" they have 
        app.moneyGoals = random.randint(10, 100)
        app.money = random.randint(int(app.moneyGoals * 0.2), int(app.moneyGoals * 0.5))
        app.time = random.randint(5, 10) #TWEAK TO BE based on life expectancy/working years of Americans 

        # Update player info
        app.player.name = app.name
        app.player.money = app.money 
        app.player.moneyGoals = app.moneyGoals
        app.player.time = app.time

        # Debugging: print player info
        print(app.player)  

        setActiveScreen('info')
    
    elif key == 'backspace':
        if len(app.name) > 0:
            app.name = app.name[:-1]
    elif key.isalpha() and key != 'space':
        app.name += str(key)
    pass  # Ignore other keys