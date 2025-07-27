import sys
from cmu_graphics import *
import random 
#---Running On Hamster Wheel Screen--------------------------------------------------------------------------------------

def run_onScreenActivate(app):
    app.numFries = random.randint(5, 10)
    app.allFriesInBag = False 

    # Generate fries at random positions in the fryer basket area (left side)
    app.fries = []
    for i in range(app.numFries):
        x = random.randint(60, 180)
        y = random.randint(150, 350)
        fry = {'x': x, 'y': y, 'inBag': False}
        app.fries.append(fry)
    app.draggingIndex = None  # No fry is being dragged at first

def run_redrawAll(app):
    drawFries(app)
    drawBag(app)
    friesInBag = sum(f['inBag'] for f in app.fries)
    drawLabel(f"Fries in bag: {friesInBag}/{app.numFries}", 
              app.width/2, 50, size=20, bold=True)
    
    if app.allFriesInBag:
        drawLabel("All fries are in the bag!\nPress Enter or Space to Collect Wage.", 
                  app.width/2, 100, size=28, fill='green', bold=True, align='center')


def drawFries(app):
    for i, fry in enumerate(app.fries):
        color = 'yellow' if not fry['inBag'] else 'gold'
        if i == app.draggingIndex:
            # When dragging, make fry bigger
            drawRect(fry['x']-3, fry['y']-18, 14, 80, fill=color, border='brown', borderWidth=2)
        else:
            drawRect(fry['x']-2, fry['y']-15, 4, 60, fill=color, border='brown')

    # fryer basket 
    drawRect(40, 120, 160, 280, fill=None, border='gray', borderWidth=4)
    drawLabel("Fryer Basket", 120, 110, size=16, bold=True)

def drawBag(app):
    bagLeft = app.width - 180
    bagTop = 200
    bagWidth = 100
    bagHeight = 140
    drawRect(bagLeft, bagTop, bagWidth, bagHeight, fill='red', border='yellow', borderWidth=4)

def run_onMousePress(app, mouseX, mouseY):
    # top fry under the mouse that is NOT in the bag
    for i in range(len(app.fries)-1, -1, -1):
        fry = app.fries[i]
        if not fry['inBag']:
            if (mouseX >= fry['x']-5 and mouseX <= fry['x']+5 and 
                mouseY >= fry['y']-20 and mouseY <= fry['y']+20):
                app.draggingIndex = i
                break

def run_onMouseDrag(app, mouseX, mouseY):
    # move fry with dragging mouse
    if app.draggingIndex is not None:
        fry = app.fries[app.draggingIndex]
        fry['x'] = mouseX
        fry['y'] = mouseY
        # Check if the fry is over the bag
        bagLeft = app.width - 180
        bagTop = 200
        bagWidth = 120
        bagHeight = 160
        if (bagLeft < fry['x'] < bagLeft + bagWidth and
            bagTop < fry['y'] < bagTop + bagHeight):
            fry['inBag'] = True
            app.draggingIndex = None  # Stop dragging
            app.allFriesInBag = all(f['inBag'] for f in app.fries)
        else:
            app.allFriesInBag = all(f['inBag'] for f in app.fries)


def run_onMouseRelease(app, mouseX, mouseY):
    # When releasing the mouse, stop dragging
    app.draggingIndex = None

def run_onKeyPress(app, key):
    if app.allFriesInBag:
        if key == 'enter' or key == 'space':
            print('REACHED: run_onKeyPress')
            app.player.money += app.hamsterMoneyAdd # Increase money by 2 for each run
            app.log.insert(0,"Made $2000 At Work")
            setActiveScreen('decision') 
    else:
        pass 