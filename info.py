import sys
from cmu_graphics import *

#---Information Screen--------------------------------------------------------------------------------------
def info_onScreenActivate(app):
    app.drawRules = False 
    pass

def info_redrawAll(app):
    # background 
    drawRect(0,0, app.width, app.height, fill = 'black')

    # drawLabel("Information Screen, space for Rules", app.width/2, 20, size=40, bold=True)
    lineHeight = 30
    if app.drawRules: 
        ruleCenter = app.height/4 - lineHeight
        drawLabel("Note:", 
                  app.width/2, ruleCenter - lineHeight,
                  fill = 'yellow', size = 30, bold = True)
        drawLabel("You are a fast food worker with three ways of making money.", 
                  app.width/2, ruleCenter,
                  fill = 'grey', size = 24, bold = True)
        drawLabel("Work quietly at your job, gamble, or invest in the stock market.", 
                  app.width/2, ruleCenter + lineHeight,
                  fill = 'grey', size = 24, bold = True)
        drawLabel("Make your choice carefully at each turn.", 
                  app.width/2,ruleCenter + 2*lineHeight,
                  fill = 'grey', size = 24, bold = True)
        drawLabel("Tip: You can backtrack from an investment choice.", 
                  app.width/2,ruleCenter + 3*lineHeight,
                  fill = 'grey', size = 24, bold = True)



    #Telling player about what they spawned in as
    drawLabel(f"{app.player.name}, life just got real.", 
              app.width/2, app.height/2 - 80, 
              fill = 'lime', size = 24, bold = True)
    drawRect(app.width/2 -150, app.height/2-30, 300,200, fill= None, border = 'yellow')
    drawLabel(f"You inherited:", 
              app.width/2, app.height/2, 
              fill = 'green', size = 24, bold = True)
    drawLabel(f"${app.player.money}",   
              app.width/2, app.height/2 + lineHeight, 
              fill = 'lime', size = 24, bold = True)
    drawLabel(f"You owe: ",
              app.width/2, app.height/2 + 2*lineHeight, 
              fill = 'red', size = 24, bold = True)
    drawLabel(f"${app.player.moneyGoals}",
              app.width/2, app.height/2 + 3*lineHeight, 
              fill = 'red', size = 24, bold = True)
    drawLabel(f"You have: {app.player.time} months. ", 
              app.width/2, app.height/2 + 5 + 4*lineHeight,
              fill = 'red', size = 24, bold = True)

    drawLabel("Hit 'Enter' to Begin Your Journey", 
              app.width/2, app.height/2 + 20 + 6*lineHeight, 
              fill = 'yellow', size = 20, bold=True)
    drawLabel("'Space' For Instructions", 
              app.width/2, app.height/2 + 20 + 7*lineHeight, 
              fill = 'forestGreen', size = 20, bold=True)

    pass

def info_onKeyPress(app, key):
    if key == 'space':
        app.drawRules = not app.drawRules #toggle app.drawRules  

    if key == 'enter':
        setActiveScreen('decision')
    else:
        pass  # Ignore other keys