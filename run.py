import sys
from cmu_graphics import *
import random 
#---Running On Hamster Wheel Screen--------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------------------------------------
#ACTUAL FRIES 
def run_onScreenActivate(app):
    app.numFries = random.randint(8, 15)
    print('run_onScreenActivate', app.numFries)
    app.fries = []
    maxTries = 50

    app.collectWageButton = (app.width//2 - 100, app.height - 130, 200, 40)


    bagWidth, bagHeight = 200, 220
    bagCenterX = app.width // 2
    bagCenterY = app.height // 2 - 70

    basketWidth = bagWidth + 80
    basketBottom = bagCenterY - bagHeight // 2 - 50

    basketCenterX = bagCenterX

    for _ in range(app.numFries):
        tries = 0
        while tries < maxTries:
            x = random.randint(basketCenterX - basketWidth//2 + Fry.fryW//2,
                                basketCenterX + basketWidth//2 - Fry.fryW//2)
            y = basketBottom - Fry.fryH//2 - 20
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

    #DECOR 

    app.bubbles = []
    app.stepsPerSecond = 20

def run_redrawAll(app):
    # background 
    drawRect(0, 0, app.width, app.height, fill='black')
    # tabletop
    drawRect(0, 0, app.width, app.height / 2, fill='black')  
    drawLine(0, app.height / 2, app.width, app.height / 2, fill='darkGray', lineWidth=3)
    drawRect(0, app.height / 2, app.width, app.height / 2, fill='gray', opacity=20)  

    for i in range(len(app.fries)):
        fry = app.fries[i]
        fry.draw(isDragging=(i == app.draggingIndex))
    drawBasket(app)
    drawBag(app)
    friesInBag = sum(fry.inBag for fry in app.fries)
    drawLabel(f"Fries in bag: {friesInBag}/{app.numFries}", 
              app.width/2, 80, fill = 'yellow', size=20, bold=True)
    if app.allFriesInBag:
        drawLabel(f"You put {app.numFries} fries in the bag.", 
                  app.width//2, app.height - 200, size=28, fill='green', bold=True, align='center')
        drawButton(app.collectWageButton, "Collect Wage")
    
    #fun drawings 
    drawLeftBasket(app)
    drawRightBasket(app)
    drawBurger(app)

def run_onMousePress(app, mouseX, mouseY):
    for i in range(len(app.fries)-1, -1, -1):
        fry = app.fries[i]
        if not fry.inBag and fry.containsPoint(mouseX, mouseY):
            app.draggingIndex = i
            break
    if app.allFriesInBag and pointInRect(mouseX, mouseY, app.collectWageButton):
        app.player.money += app.hamsterMoneyAdd
        app.log.insert(0, "+$2000 Work")
        setActiveScreen('decision')

def run_onKeyPress(app, key):
    if app.allFriesInBag:
        if key == 'enter' or key == 'space':
            print('REACHED: run_onKeyPress')
            app.player.money += app.hamsterMoneyAdd # Increase money by 2 for each run
            app.log.insert(0,"+$2000 Work")
            setActiveScreen('decision') 
    else:
        pass 

def run_onMouseDrag(app, mouseX, mouseY):
    if app.draggingIndex is not None:
        fry = app.fries[app.draggingIndex]
        #fry.x = mouseX
        #fry.y = mouseY

        mouseWait=10
        dx,dy=mouseX-fry.x,mouseY-fry.y
        if dx>mouseWait:#mouse moving too quickly
            fry.x+=mouseWait
        elif dx<-mouseWait:#mouse moving too quickly
            fry.x-=mouseWait
        else:
            fry.x=mouseX
        if dy>mouseWait:#mouse moving too quickly
            fry.y+=mouseWait
        elif dx<-mouseWait:#mouse moving too quickly
            fry.y-=mouseWait
        else:
            fry.y=mouseY


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
            app.draggingIndex = None
            # Update allFriesInBag
            app.allFriesInBag = all(fry.inBag for fry in app.fries)
        else:
            app.allFriesInBag = all(fry.inBag for fry in app.fries)

def run_onMouseRelease(app, mouseX, mouseY):
    app.draggingIndex = None

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

    # Draw the plate 
    drawOval(ovalX, 618, ovalWidth, ovalHeight, fill='slateGray', border='black', borderWidth = 4)

    drawRect(bagLeft, bagTop, bagWidth, bagHeight, 
             fill='red', border='black', borderWidth=4, align = 'center')
    drawLabel(f"Just put the fries", 
              bagLeft, bagTop, size = 15,  align = 'center', bold = True)
    drawLabel(f"in the bag", 
              bagLeft, bagTop + 20, size = 15, align = 'center', bold = True)
    drawLabel(f"M", 
              bagLeft, bagTop - 30, size = 40, 
              font = 'comic sans', 
              fill = 'yellow', align = 'center', bold = True)
   
# HELPER
def drawButton(rect, label):
    x, y, w, h = rect
    drawRect(x, y, w, h, fill='green', border='darkGreen', borderWidth=2)
    drawLabel(label, x + w//2, y + h//2, size=18, fill='lime', bold=True)

def pointInRect(x, y, rect):
    rx, ry, rw, rh = rect
    return (rx <= x <= rx + rw) and (ry <= y <= ry + rh)
  
    


# DECOR 

def drawBurger(app):
    centerX = app.width // 4
    baseY = app.height // 2 + 130

    # Bottom bun
    drawOval(centerX, baseY, 100, 50, fill='burlywood', border='saddleBrown', borderWidth=2)

    # Patty
    drawRect(centerX, baseY - 25, 100, 20, fill='sienna', align='center', border='black')

    # Cheese
    drawPolygon(centerX - 50, baseY - 35, centerX, baseY - 50, centerX + 50, baseY - 35,
                centerX, baseY - 20, fill='gold', border='goldenrod')

    # Lettuce
    drawOval(centerX, baseY - 55, 110, 20, fill='darkGreen', opacity=70)

    # Top bun
    drawOval(centerX, baseY - 80, 120, 50, fill='burlywood', border='saddleBrown', borderWidth=2)

    #Stick through bun 
    drawLine(centerX, baseY-80, centerX, baseY - 120, fill = 'red', lineWidth = 4)



def drawLeftBasket(app):
    drawBubbles(app)
    bagWidth, bagHeight = 200, 220
    bagCenterY = app.height // 2 - 70  # Same vertical placement as main basket

    basketWidth = bagWidth + 80
    basketHeight = 50

    basketBottom = bagCenterY - bagHeight // 2 - 50
    basketTop = basketBottom - basketHeight
    basketCenterY = (basketTop + basketBottom) // 2

    basketCenterX = app.width // 5  # 20% of screen width
    basketLeft = basketCenterX - basketWidth // 2

    oilHeight = basketHeight // 2
    oilCenterY = basketCenterY + oilHeight // 2

    drawRect(basketCenterX, oilCenterY, basketWidth, oilHeight,
             fill='white', align='center')
    drawRect(basketCenterX, oilCenterY, basketWidth, oilHeight,
             fill='yellow', opacity=40, align='center')

    for i in range(1, basketHeight, 15):
        drawLine(basketLeft, basketTop + i * 0.8,
                 basketLeft + basketWidth, basketTop + i * 0.8,
                 opacity=80, fill='lightGrey')

    drawRect(basketCenterX, basketCenterY, basketWidth, basketHeight,
             fill=None, border='gray', borderWidth=5, align='center')

def drawRightBasket(app):
    drawBubbles(app)
    bagWidth, bagHeight = 200, 220
    bagCenterY = app.height // 2 - 70  # Same vertical alignment

    basketWidth = bagWidth + 80
    basketHeight = 50

    basketBottom = bagCenterY - bagHeight // 2 - 50
    basketTop = basketBottom - basketHeight
    basketCenterY = (basketTop + basketBottom) // 2

    basketCenterX = app.width * 4 // 5
    basketLeft = basketCenterX - basketWidth // 2

    oilHeight = basketHeight // 2
    oilCenterY = basketCenterY + oilHeight // 2

    drawRect(basketCenterX, oilCenterY, basketWidth, oilHeight,
             fill='white', align='center')
    drawRect(basketCenterX, oilCenterY, basketWidth, oilHeight,
             fill='yellow', opacity=40, align='center')

    for i in range(1, basketHeight, 15):
        drawLine(basketLeft, basketTop + i * 0.8,
                 basketLeft + basketWidth, basketTop + i * 0.8,
                 opacity=80, fill='lightGrey')

    drawRect(basketCenterX, basketCenterY, basketWidth, basketHeight,
             fill=None, border='gray', borderWidth=5, align='center')
#BUBBLES 

def run_onStep(app):
    # Occasionally create bubbles on both sides
    if random.random() < 0.5:
        for side in ['left', 'right']:
            if side == 'left':
                x = app.width // 5 + random.randint(-50, 50)
            else:
                x = app.width * 4 // 5 + random.randint(-50, 50)
            y = app.height // 2 - 280  # Top of oil
            r = random.randint(4, 10)
            opacity = 100
            app.bubbles.append([x, y, r, opacity])

    # Animate bubbles upward and fading
    for bubble in app.bubbles:
        bubble[1] -= 1.5  # move up
        bubble[3] -= 2    # fade

    # Remove invisible or out-of-bound bubbles
    app.bubbles = [b for b in app.bubbles if b[1] > app.height // 2 - 300 and b[3] > 0]

def drawBubbles(app):
    for x, y, r, _ in app.bubbles:
        drawOval(x, y, r, r, fill='yellow', border = 'orange', opacity=60)
        drawOval(x, y, r, r, fill='white', border = 'orange', opacity=60)