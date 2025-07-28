import sys
from cmu_graphics import *
import random 
#---Running On Hamster Wheel Screen--------------------------------------------------------------------------------------
#Define Class Fry 
class Fry:
    fryW, fryH = 10, 60  # Class-wide size

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inBag = False

    def draw(self, isDragging=False):
        color = 'orange' if self.inBag else 'yellow'
        w, h = Fry.fryW, Fry.fryH
        if isDragging:
            drawRect(self.x - w//2 - 1, self.y - h//2 - 3, w + 2, h + 6, fill=color, border='brown', borderWidth=3)
        else:
            drawRect(self.x - w//2, self.y - h//2, w, h, fill=color, border='brown', borderWidth=2)

    def overlaps(self, other):
        # Returns True if this fry overlaps another fry
        w, h = Fry.fryW, Fry.fryH
        left1, right1 = self.x - w//2, self.x + w//2
        top1, bottom1 = self.y - h//2, self.y + h//2
        left2, right2 = other.x - w//2, other.x + w//2
        top2, bottom2 = other.y - h//2, other.y + h//2
        return not (right1 < left2 or left1 > right2 or bottom1 < top2 or top1 > bottom2)

    def containsPoint(self, x, y):
        w, h = Fry.fryW, Fry.fryH
        return (self.x - w//2 <= x <= self.x + w//2) and (self.y - h//2 <= y <= self.y + h//2)

#ACTUAL FRIES 
def run_onScreenActivate(app):
    app.numFries = random.randint(8, 15)
    print('run_onScreenActivate', app.numFries)
    app.fries = []
    maxTries = 50
    for _ in range(app.numFries):
        tries = 0
        while tries < maxTries:
            x = random.randint(60 + Fry.fryW//2, 180 - Fry.fryW//2)
            y = random.randint(150 + Fry.fryH//2, 350 - Fry.fryH//2)
            newFry = Fry(x, y)
            overlap = False
            for fry in app.fries:
                if newFry.overlaps(fry):
                    overlap = True
                    break
            if not overlap:
                app.fries.append(newFry)
                break
            tries += 1
    app.draggingIndex = None
    app.allFriesInBag = False

def run_redrawAll(app):
    for i in range(len(app.fries)):
        fry = app.fries[i]
        fry.draw(isDragging=(i == app.draggingIndex))
    drawRect(40, 120, 160, 280, fill=None, border='gray', borderWidth=4)
    drawLabel("Fryer Basket", 120, 110, size=16, bold=True)
    drawBag(app)
    friesInBag = sum(fry.inBag for fry in app.fries)
    drawLabel(f"Fries in bag: {friesInBag}/{app.numFries}", app.width/2, 50, size=20, bold=True)
    if app.allFriesInBag:
        drawLabel("You put all the fries in the bag!\nPress Enter or Space to continue.", app.width/2, 100, size=28, fill='green', bold=True, align='center')


def drawBag(app):
    bagLeft = app.width - 180
    bagTop = 200
    bagWidth = 180
    bagHeight = 200
    drawRect(bagLeft, bagTop, bagWidth, bagHeight, fill='red', border='yellow', borderWidth=4)

def run_onMousePress(app, mouseX, mouseY):
    for i in range(len(app.fries)-1, -1, -1):
        fry = app.fries[i]
        if not fry.inBag and fry.containsPoint(mouseX, mouseY):
            app.draggingIndex = i
            break

def run_onMouseDrag(app, mouseX, mouseY):
    if app.draggingIndex is not None:
        fry = app.fries[app.draggingIndex]
        fry.x = mouseX
        fry.y = mouseY
        bagLeft = app.width - 180
        bagTop = 200
        bagWidth = 120
        bagHeight = 160
        if (bagLeft < fry.x < bagLeft + bagWidth and
            bagTop < fry.y < bagTop + bagHeight):
            fry.inBag = True
            app.draggingIndex = None
            # Update allFriesInBag
            app.allFriesInBag = all(fry.inBag for fry in app.fries)
        else:
            app.allFriesInBag = all(fry.inBag for fry in app.fries)

def run_onMouseRelease(app, mouseX, mouseY):
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