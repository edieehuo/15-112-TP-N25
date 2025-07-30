from cmu_graphics import *
from tracker import *
import random
import math

#---Lottery Screen--------------------------------------------------------------------------------------
def lottery_onScreenActivate(app):
    app.hasGambled = False 
    app.gambledMoney = 0
    app.gambleInput = ''

    app.gambleBox = (app.width/2, app.height - 200, 140, 80)

    app.showResult = False
    app.resultText = ''

    app.options = [0, 0.5, 1, 2, 5]  # Multipliers
    app.spinnerLabels = ['>:)' , ':|', ':}', ' :D', ':)']
    app.colors = ['red', 'orange', 'purple', 'blue','green']

    app.selectedMultiplier = None
    app.numSections = len(app.options)
    app.spinnerAngle = 0
    app.spinnerSpeed = 0
    app.spinning = False
    app.wheelX = app.width / 2 
    app.wheelY = app.height / 2 
    app.wheelRad = 160

def lottery_redrawAll(app):
    # drawLabel("Lottery Screen", app.width/2, 20, size=40, bold=True)
    #draw bg 
    drawRect(0,0, app.width, app.height, fill = 'black')
    drawDecor(app)

    #draw tracker 
    tracker_redrawAll(app)

    #draw player input 
    drawLabel(f"Enter Amount To Gamble:", 
              app.width/2, app.height//4 - 80, 
              fill = 'yellow', size = 40, bold = True)
    
    drawLabel(f"${app.gambleInput}", 
              app.width/2, app.height//4 - 30, 
              fill = 'yellow', size = 30)

    #draw Spinner 
    drawSpinner(app)

    #draw gamble button for not gambled yet 
    if not app.hasGambled: 
        drawGambleButton(app)

    #after gambled 
    if app.showResult:
        drawLabel(app.resultText, 
                  app.width/2, app.height/2 + 185, 
                  fill = 'yellow', size=24, bold = True)
        if app.hasGambled:
            drawLabel("Press D to Return to Decision Screen", 
                      app.width/2, app.height/2 + 240, 
                      fill = 'lime', size=20, bold = True )


def lottery_onStep(app):
    if app.spinning:
        app.spinnerAngle += app.spinnerSpeed
        app.spinnerSpeed *= 0.95  # friction
        if app.spinnerSpeed < 0.1:
            app.hasGambled =True 
            app.spinning = False
            app.spinnerAngle %= 360
            sectionAngle = 360 / app.numSections

            #B UG BUGB BUGBUGGUBGBGUBG 
            selectedIndex = int(((app.numSections - (app.spinnerAngle % 360) / sectionAngle)+1) % app.numSections)
            app.selectedMultiplier = app.options[selectedIndex]
            winnings = int(app.gambledMoney * app.selectedMultiplier)
            app.player.money += winnings
            app.resultText = getResultText(app, winnings)
            app.showResult = True

def lottery_onKeyPress(app, key):
    if key.isdigit():
        app.gambleInput += key
    elif key == 'backspace':
        app.gambleInput = app.gambleInput[:-1]
    if app.hasGambled:
        if key == 'd':
            setActiveScreen('decision')

def lottery_onMousePress(app, mouseX, mouseY):
    x, y, w, h = app.gambleBox
    if not app.hasGambled: 
        if (x <= mouseX <= x+w) and (y <= mouseY <= y+h):
            if app.gambleInput.isdigit():
                app.gambledMoney = int(app.gambleInput)
                app.hasGambled = True 
                if app.gambledMoney > 0 and app.gambledMoney <= app.player.money:
                    app.player.money -= app.gambledMoney
                    spinSpinner(app)
                else:
                    resetApp(app)
            else:
                resetApp(app)

def resetApp(app):
    app.hasGambled = False 
    app.gambledMoney = 0
    app.gambleInput = ''

    app.gambleBox = (app.width/2, app.height - 200, 140, 80)
    
    app.showResult = False
    app.resultText = ''

    app.options = [0, 0.5, 1, 2, 5]  # Multipliers
    app.spinnerLabels = ['>:)' , ':|', ':}', ' :D', ':)']
    app.colors = ['red', 'orange', 'purple', 'blue','green']

    app.selectedMultiplier = None
    app.numSections = len(app.options)
    app.spinnerAngle = 0
    app.spinnerSpeed = 0
    app.spinning = False
    app.wheelX = app.width / 2 
    app.wheelY = app.height / 2 
    app.wheelRad = 160


def getResultText(app,winnings):
    if winnings < app.gambledMoney:
        if winnings == 0:
            app.log.insert(0,f"-${app.gambledMoney} Gambling")
            return f"Better luck next time."
        app.log.insert(0,f"-${winnings} Gambling")
        return f"Better luck next time."
    else: 
        app.log.insert(0,f"+${winnings} Gambling")
        return f'${winnings} in winnings.'

def spinSpinner(app):
    app.spinnerSpeed = random.uniform(40, 90)
    app.spinning = True
    app.showResult = False
    app.resultText = ''




#DRAW FUNCTIONS -----------------------------------------------------------------------------------------------------

def drawSpinner(app):
    sectionAngle = 360 / app.numSections
    for i in range(app.numSections):
        start = math.radians(i * sectionAngle + app.spinnerAngle)
        end = math.radians((i+1) * sectionAngle + app.spinnerAngle)
        mid = math.radians((i + 0.5) * sectionAngle + app.spinnerAngle)
        x1, y1 = app.wheelX, app.wheelY
        x2 = x1 + app.wheelRad * math.cos(start)
        y2 = y1 - app.wheelRad * math.sin(start)
        x3 = x1 + app.wheelRad * math.cos(end)
        y3 = y1 - app.wheelRad * math.sin(end)
        drawPolygon(x1, y1, x2, y2, x3, y3, fill=app.colors[i], border = 'lime', borderWidth = 3)

        labelX = x1 + (app.wheelRad/1.5) * math.cos(mid)
        labelY = y1 - (app.wheelRad/1.5) * math.sin(mid)
        drawCircle(labelX,labelY,15, fill = 'yellow', border = 'black')
        drawLabel(f"{app.spinnerLabels[i]}", labelX, labelY, size=14, bold = True, fill = 'black')

    drawPolygon(app.wheelX, app.wheelY - app.wheelRad - 5,
                app.wheelX - 10, app.wheelY - app.wheelRad - 25,
                app.wheelX + 10, app.wheelY - app.wheelRad - 25,
                fill='red')

def drawGambleButton(app):
    x, y, w, h = app.gambleBox
    drawRect(x, y, w, h, fill='green', border='lime', borderWidth = 4, align = 'center')
    drawLabel("Gamble", x, y, size=16, fill='lime', bold=True)

def drawDecor(app):
    drawRect(0,0, app.width, app.height, fill = 'black', opacity = 20)

    # drawLine(200,0,200,app.height, fill = 'yellow', lineWidth = 10)
    drawCircle(0,0, app.width, fill = None, border = 'yellow')
    drawCircle(15,0, app.width, fill = None, border = 'orangeRed', borderWidth = 3)
    drawCircle(40,0, app.width, fill = None, border = 'maroon', borderWidth = 5)
    drawCircle(66,0, app.width, fill = None, border = 'yellow', borderWidth = 8)
    drawCircle(80,0, app.width, fill = None, border = 'orangeRed', borderWidth = 10)
    drawCircle(90,0, app.width, fill = None, border = 'maroon', borderWidth = 15)
    drawCircle(110,0, app.width, fill = None, border = 'green')
    drawCircle(140,0, app.width, fill = None, border = 'orangeRed', borderWidth = 3)
    drawCircle(166,0, app.width, fill = None, border = 'purple', borderWidth = 8)
    drawCircle(180,0, app.width, fill = None, border = 'blue', borderWidth = 10)
    drawCircle(190,0, app.width, fill = None, border = 'lime', borderWidth = 15)