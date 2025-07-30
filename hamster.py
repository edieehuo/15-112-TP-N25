import sys
from cmu_graphics import *
from run import *


#---Hamster Wheel Screen--------------------------------------------------------------------------------------
#INCORPORATE INFO ABOUT HAMSTER WHEEL AND HOW TO PLAY HAMSTER WHEEL 

def hamster_onScreenActivate(app):
    app.screenName = 'hamster'
    app.hamsterMoneyAdd = 2000

    app.goToWorkButton = (app.width//2 - 100, app.height - 130, 200, 40)
    
    app.numTrainingFries = random.randint(2,5)
    app.trainingFries = []

    maxTries = 50 
    bagWidth, bagHeight = 200, 220
    bagCenterX = app.width // 2
    bagCenterY = app.height // 2 - 70

    basketWidth = bagWidth + 80
    basketBottom = bagCenterY - bagHeight // 2 - 50

    basketCenterX = bagCenterX

    for _ in range(app.numTrainingFries):
        tries = 0
        while tries < maxTries:
            x = random.randint(basketCenterX - basketWidth//2 + Fry.fryW//2,
                                basketCenterX + basketWidth//2 - Fry.fryW//2)
            y = basketBottom - Fry.fryH//2 - 20
            newFry = Fry(x, y)
            overlap = False
            for fry in app.trainingFries:
                if newFry.overlaps(fry):
                    overlap = True
                    break
            if not overlap:
                app.trainingFries.append(newFry)
                break
            tries += 1

    app.fryDraggingIndex = None
    app.allTrainingFriesInBag = False

    pass 

def hamster_onMousePress(app, mouseX, mouseY):
    if app.allTrainingFriesInBag and pointInRect(mouseX, mouseY, app.goToWorkButton):
        setActiveScreen('run')

    for i in range(len(app.trainingFries)-1, -1, -1):
        fry = app.trainingFries[i]
        if not fry.inBag and fry.containsPoint(mouseX, mouseY):
            app.fryDraggingIndex = i
            break

def pointInRect(x, y, rect):
    rx, ry, rw, rh = rect
    return (rx <= x <= rx + rw) and (ry <= y <= ry + rh)

def hamster_onMouseDrag(app, mouseX, mouseY):
    if app.fryDraggingIndex is not None:
        fry = app.trainingFries[app.fryDraggingIndex]
        fry.x = mouseX
        fry.y = mouseY

        bagWidth = 200
        bagHeight = 220
        bagCenterX = app.width // 2
        bagCenterY = app.height // 2 + 50

        bagLeft = bagCenterX - bagWidth // 2
        bagRight = bagCenterX + bagWidth // 2
        bagTop = bagCenterY - bagHeight // 2
        bagBottom = bagCenterY + bagHeight // 2

        if (bagLeft < fry.x < bagRight and
            bagTop < fry.y < bagBottom):
            fry.inBag = True
            app.fryDraggingIndex = None
            # Update allFriesInBag
            app.allTrainingFriesInBag = all(fry.inBag for fry in app.trainingFries)
        else:
            app.allTrainingFriesInBag = all(fry.inBag for fry in app.trainingFries)

def hamster_onMouseRelease(app, mouseX, mouseY):
    app.fryDraggingIndex = None
def hamster_redrawAll(app):
    drawLabel("Hamster Screen", app.width/2, 10, size=40, bold=True)
    # drawLabel("Press R to Run", app.width/2, app.height/2)

    # background 
    drawRect(0, 0, app.width, app.height, fill='black')
    # tabletop
    drawRect(0, 0, app.width, app.height / 2, fill='black')  
    drawLine(0, app.height / 2, app.width, app.height / 2, fill='darkGray', lineWidth=3)
    drawRect(0, app.height / 2, app.width, app.height / 2, fill='gray', opacity=20)  

    for i in range(len(app.trainingFries)):
        fry = app.trainingFries[i]
        fry.draw(isDragging=(i == app.fryDraggingIndex))
    drawBasket(app)
    drawBag(app)
    friesInBag = sum(fry.inBag for fry in app.trainingFries)
    drawLabel(f"Fries in bag: {friesInBag}/{app.numTrainingFries}", 
              app.width/2, 80, fill = 'yellow', size=20, bold=True)
    if not app.allTrainingFriesInBag:
        drawLabel(f"Click on, then drag each fry from fryer to bag. ", 
                  app.width//2, app.height - 200, size=28, fill='yellow', bold=True, align='center')
    if app.allTrainingFriesInBag:
        drawLabel(f"Completed Training.", 
                  app.width//2, app.height - 200, size=28, fill='green', bold=True, align='center')
        drawButton(app.goToWorkButton, "Go to Work")

def drawButton(rect, label):
    x, y, w, h = rect
    drawRect(x, y, w, h, fill='green', border='darkGreen', borderWidth=2)
    drawLabel(label, x + w//2, y + h//2, size=18, fill='lime', bold=True)

def drawBasket(app):
    bagWidth, bagHeight = 200, 220
    bagCenterX = app.width // 2
    bagCenterY = app.height // 2 - 70

    basketWidth = bagWidth + 80
    basketHeight = 50

    basketBottom = bagCenterY - bagHeight // 2 - 50
    basketTop = basketBottom - basketHeight

    basketCenterX = bagCenterX
    basketLeft = basketCenterX - basketWidth//2
    basketCenterY = (basketTop + basketBottom) // 2
    
    oilHeight = basketHeight // 2
    oilCenterY = basketCenterY + oilHeight // 2  # Oil is in the lower half

    drawRect(basketCenterX, oilCenterY, basketWidth, oilHeight,
         fill='white', align='center')
    drawRect(basketCenterX, oilCenterY, basketWidth, oilHeight,
         fill='yellow', opacity=40, align='center')
    for i in range(1, basketHeight, 15):
        drawLine(basketLeft, basketTop + i*0.8, basketLeft + basketWidth, basketTop + i*0.8, opacity = 80, fill = 'lightGrey')
    drawRect(basketCenterX, basketCenterY, basketWidth, basketHeight, fill=None, border='gray', borderWidth=5, align='center')


def drawBag(app):
    bagLeft = app.width//2
    bagTop = app.height//2 + 50
    bagWidth = 200
    bagHeight = 220

    #plate 
    ovalWidth = bagWidth * 1.5  # Oval is 1.5 times the width of the bag
    ovalHeight = 50  # Set height for the oval (larger to represent a plate)
    
    # Position the oval so that it overlaps half with the fries bag
    ovalX = bagLeft  # Centered horizontally under the bag

    # Draw the oval (plate, shadow, or visual effect)
    drawOval(ovalX, 618, ovalWidth, ovalHeight, fill='slateGray', border='black', borderWidth = 4)

    drawRect(bagLeft, bagTop, bagWidth, bagHeight, 
             fill='red', border='black', borderWidth=4, align = 'center')
    drawLabel(f"MANDATORY TRAINING", 
              bagLeft, bagTop, size = 15,  align = 'center', bold = True)
    drawLabel(f"MODULE", 
              bagLeft, bagTop + 20, size = 15, align = 'center', bold = True)
    
    

