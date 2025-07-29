from cmu_graphics import *
from tracker import *
import random
import math

#---Lottery Screen--------------------------------------------------------------------------------------
def lottery_onScreenActivate(app):
    app.hasGambled = False 
    app.gambledMoney = 0
    app.gambleInput = ''
    app.gambleBox = (app.width/2 - 60, app.height - 100, 120, 40)

    app.showResult = False
    app.resultText = ''
    app.options = [0, 0.5, 1, 2, 5]  # Multipliers
    app.colors = ['red', 'orange', 'yellow', 'blue','green']
    app.selectedMultiplier = None
    app.numSections = len(app.options)
    app.spinnerAngle = 0
    app.spinnerSpeed = 0
    app.spinning = False
    app.wheelX = app.width / 2
    app.wheelY = app.height / 2 - 50
    app.wheelRad = 160

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

def getResultText(app,winnings):
    if winnings < app.gambledMoney:
        app.log.insert(0,f"Lost ${winnings} Gambling")
        return f'oops, lost ${winnings}'
    else: 
        app.log.insert(0,f"Made ${winnings} Gambling")
        return f'yay! made ${winnings}'

def spinSpinner(app):
    app.spinnerSpeed = random.uniform(40, 90)
    app.spinning = True
    app.showResult = False
    app.resultText = ''

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
        drawPolygon(x1, y1, x2, y2, x3, y3, fill=app.colors[i])

        labelX = x1 + (app.wheelRad/1.5) * math.cos(mid)
        labelY = y1 - (app.wheelRad/1.5) * math.sin(mid)
        drawLabel(f"{app.options[i]}x", labelX, labelY, size=14)

    drawPolygon(app.wheelX, app.wheelY - app.wheelRad - 5,
                app.wheelX - 10, app.wheelY - app.wheelRad - 25,
                app.wheelX + 10, app.wheelY - app.wheelRad - 25,
                fill='red')

def drawGambleButton(app):
    x, y, w, h = app.gambleBox
    drawRect(x, y, w, h, fill='green', border='black')
    drawLabel("Gamble", x + w/2, y + h/2, size=16, bold=True)

def lottery_redrawAll(app):
    tracker_redrawAll(app)
    drawLabel("Lottery Screen", app.width/2, 20, size=40, bold=True)

    drawLabel(f"Enter Gamble Amount:", app.width/2, 60, size=40)
    drawLabel(f"${app.gambleInput}", app.width/2, 90, size=20)

    drawSpinner(app)

    if not app.hasGambled: 
        drawGambleButton(app)

    if app.showResult:
        drawLabel(app.resultText, app.width/2, app.height/2 + 100, size=22, bold=True)
        drawLabel("Press D to Return to Decision Screen", app.width/2, app.height - 40, size=14)

def lottery_onKeyPress(app, key):
    if key.isdigit():
        app.gambleInput += key
    elif key == 'backspace':
        app.gambleInput = app.gambleInput[:-1]
    if app.hasGambled:
        if key == 'd':
            setActiveScreen('decision')

def lottery_onMousePress(app, mouseX, mouseY):
    # if hasattr(app, 'gambleBox'):
    x, y, w, h = app.gambleBox
    if not app.hasGambled: 
        if (x <= mouseX <= x+w) and (y <= mouseY <= y+h):
            if app.gambleInput.isdigit():
                app.gambledMoney = int(app.gambleInput)
                if app.gambledMoney > 0 and app.gambledMoney <= app.player.money:
                    app.player.money -= app.gambledMoney
                    spinSpinner(app)
                else:
                    app.resultText = "Invalid bet amount!"
                    app.showResult = True
            else:
                app.resultText = "Enter a number first!"
                app.showResult = True
