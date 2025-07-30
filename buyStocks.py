from cmu_graphics import *
from player import Player
from info import *

# INVESTMENT IMPORTS
from investment import *
from stocks import *

def buyStocks_onScreenActivate(app):
    app.buyStockNum = None
    app.tooBroke = False
    app.showHoldings = False

    # Layout for Buy and View buttons
    buttonW, buttonH = 150, 35
    spacing = 15
    left = app.width // 2 - buttonW // 2
    top = 300

    app.buyButton = (left, top, buttonW, buttonH)
    app.toggleHoldingsButton = (left, top + buttonH + spacing, buttonW, buttonH)


def buyStocks_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    # drawLabel("BUY STOCKS", app.width // 2, 40, size=36, fill='lime', bold=True)

    infoX = 100
    infoY = 220
    drawLabel("Market Stock Info:", infoX, infoY, size=20, fill='white', bold=True, align='left')
    drawLabel(f"Price: ${app.stockInfo.stockPrice}", infoX, infoY + 30, size=16, fill='lightGray', align='left')
    drawLabel(f"Volatility: {app.stockInfo.stockVolatility}%", infoX, infoY + 55, size=16, fill='lightGray', align='left')

    y = 120
    if app.buyStockNum is None:
        drawLabel("Type a number (1–9) to choose how many stocks to buy.", 
                  app.width // 2, y, size=20, fill='white', bold=True)
    else:
        total = app.buyStockNum * app.stockInfo.stockPrice
        drawLabel(f"You chose to buy {app.buyStockNum} stock(s)", app.width // 2, y, size=20, fill='white', bold=True)
        drawLabel(f"Total: ${total}", app.width // 2, y + 30, size=18, fill='lightGray')

    if app.tooBroke:
        drawLabel(f" Not enough money to buy {app.buyStockNum} stock(s).", 
                  app.width // 2, y + 70, size=20, fill='red', bold=True)

    if app.buyStockNum is not None:
        drawButton(app.buyButton, f"Buy {app.buyStockNum}")
    drawButton(app.toggleHoldingsButton, "Hide Holdings" if app.showHoldings else "View Holdings")

    if app.showHoldings and app.playerPortfolio and app.playerPortfolio.numDiffStocks > 0:
        drawHorizontalPortfolio(app)


def buyStocks_onMousePress(app, mouseX, mouseY):
    if pointInRect(mouseX, mouseY, app.toggleHoldingsButton):
        app.showHoldings = not app.showHoldings
    elif pointInRect(mouseX, mouseY, app.buyButton) and app.buyStockNum is not None:
        if canBuy(app):  
            app.tooBroke = False 
            app.log.insert(0, f'Invested ${app.invested} in Stocks')
            app.invested = 0
            app.player.money -= app.stockInfo.stockPrice * app.buyStockNum
            app.playerPortfolio.addStock(app.stockInfo.stockPrice, app.stockInfo.stockVolatility, app.buyStockNum)
            setActiveScreen('decision')
        else:
            app.tooBroke = True

def buyStocks_onKeyPress(app, key):
    if key.isdigit() and key != '0':
        app.buyStockNum = int(key)
        app.tooBroke = False

def canBuy(app): 
    total = app.buyStockNum * app.stockInfo.stockPrice
    if total <= app.player.money:
        app.invested = total
        return True
    return False

def drawButton(rect, label):
    x, y, w, h = rect
    drawRect(x, y, w, h, fill='dimGrey', border='white', borderWidth=2)
    drawLabel(label, x + w // 2, y + h // 2, size=14, fill='white', bold=True)

def pointInRect(x, y, rect):
    rx, ry, rw, rh = rect
    return (rx <= x <= rx + rw) and (ry <= y <= ry + rh)

# Horizontal layout of portfolio holdings
def drawHorizontalPortfolio(app):
    drawLabel("Your Holdings:", app.width // 2, 420, fill='lime', size=20, bold=True)

    spacingX = 240
    startY = 450
    wrapThreshold = app.width - 60

    x = 60
    y = startY

    i = 0
    if app.playerPortfolio.numDiffStocks == 0 :
        drawLabel(f"None Held!", x, y, size=14, fill='white', bold=True, align='left')
    for stock in app.playerPortfolio.stocks:
        buyPrice, vol = stock
        stockData = app.playerPortfolio.stocks[stock]
        numHeld = stockData['numHeld']
        newValue = stockData['newValue']
        marketPrice = newValue // numHeld if numHeld > 0 else '—'

        drawLabel(f"Stock {i+1}", x, y, size=14, fill='white', bold=True, align='left')
        drawLabel(f"${buyPrice} → ${marketPrice} | {numHeld} shares", x, y + 18, size=12, fill='lightGray', align='left')

        x += spacingX
        if x > wrapThreshold:
            x = 60
            y += 50

        i += 1
