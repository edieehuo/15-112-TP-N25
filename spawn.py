import sys
from cmu_graphics import *
import random

#---Spawn Screen--------------------------------------------------------------------------------------
def spawn_onScreenActivate(app):
    app.screenName = 'spawn'
    app.name = ''  # Initialize name as an empty string
    pass 

def spawn_redrawAll(app):
    drawLabel("Spawning Screen", app.width/2, 10, size=40, bold=True)
    # background 
    drawRect(0,0, app.width, app.height, fill = 'black')

    drawLabel("Enter Player Name:", 
              app.width/2, app.height/2 - 50, 
              fill = 'green', size = 24, bold = True )
    drawLabel(app.name, 
              app.width/2, app.height/2 + 10, 
              size=24, bold = True, fill = 'white', font = 'monospace')
    
    nameLength = len(app.name)
    charWidth = 20  #width of char
    lineWidth = nameLength * charWidth 

    drawLine(app.width/2 - lineWidth/2, app.height/2 + 50,
            app.width/2 + lineWidth/2, app.height/2 + 50,
            fill='white')
    
    if app.name: 
        drawLabel(" Press Enter To Continue", 
                app.width/2, app.height/2 + 100,
                fill = 'green', size = 24, bold = True)

def spawn_onKeyPress(app, key):
    if key == 'enter':
        # Generate goalmoney, starting money, number of "years" they have 
        app.moneyGoals = random.randint(10, 100)*1000
        app.money = random.randint(int(app.moneyGoals * 0.2), int(app.moneyGoals * 0.5))
        app.time = random.randint(10, 20) #TWEAK TO BE based on life expectancy/working years of Americans 

        # Update player info
        app.player.name = app.name
        app.player.money = app.money 
        app.player.moneyGoals = app.moneyGoals
        app.player.time = app.time

        setActiveScreen('info')
    
    elif key == 'backspace':
        if len(app.name) > 0:
            app.name = app.name[:-1]
    elif key.isalpha() and key != 'space':
        app.name += str(key)
    pass  # Ignore other keys