from cmu_graphics import *
import math
from player import *
from info import *
from decision import *
from investment import *
from stocks import *

def sellStocks_onScreenActivate(app):
    app.sellAmount = 0
    app.sellStockNum = None
    app.showHoldings = False
    # app.drawNothingToSell = (app.playerPortfolio.numDiffStocks == 0)

    # Buttons
    buttonW, buttonH = 150, 35
    spacing = 15
    centerX = app.width // 2
    top = 300

    app.sellButton = (centerX - buttonW // 2, top, buttonW, buttonH)
    app.toggleHoldingsButton = (centerX - buttonW // 2, top + buttonH + spacing, buttonW, buttonH)
    app.returnToStocksButton = (centerX - buttonW // 2, app.height // 2 + 40, buttonW, buttonH)

def sellStocks_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    if len(app.playerPortfolio.stocks) == 0:
        drawNothingToSell(app)
        return
    # Left Panel
    infoX = 100
    infoY = 140
    drawLabel("Selected Stock Info:", infoX, infoY, size=20, fill='white', bold=True, align='left')
    if app.sellStockNum is not None:
        stockKey = list(app.playerPortfolio.stocks.keys())[app.sellStockNum]
        strikePrice, volatility = stockKey
        stock = app.playerPortfolio.stocks[stockKey]
        numHeld = stock['numHeld']
        newValue = stock['newValue']
        marketPrice = newValue // numHeld if numHeld > 0 else '—'

        drawLabel(f"Buy: ${strikePrice}", infoX, infoY + 30, size=16, fill='lightGray', align='left')
        drawLabel(f"Market: ${marketPrice}", infoX, infoY + 50, size=16, fill='lightGray', align='left')
        drawLabel(f"Shares: {numHeld}", infoX, infoY + 70, size=16, fill='lightGray', align='left')
        drawLabel(f"Volatility: {volatility}%", infoX, infoY + 90, size=16, fill='lightGray', align='left')
    else:
        drawLabel("Select a stock with keys 1–9", infoX, infoY + 30, size=16, fill='lightGray', align='left')

    # Center: Instructions
    centerY = 120
    if app.sellStockNum is None:
        drawLabel("Type 1–9 to select a stock to sell", app.width // 2, centerY, size=20, fill='white', bold=True)
    else:
        drawLabel(f"Selected Stock {app.sellStockNum + 1}", app.width // 2, centerY, size=20, fill='lime', bold=True)
        drawLabel("Press number to select quantity", app.width // 2, centerY + 30, size=16, fill='lightGray')
        drawLabel("Press C to choose another stock", app.width // 2, centerY + 50, size=14, fill='gray')

    if app.sellAmount > 0:
        drawLabel(f"Amount to Sell: {app.sellAmount}", app.width // 2, centerY + 80, size=18, fill='lime', bold=True)

    # Buttons
    drawButton(app.toggleHoldingsButton, "View Holdings" if not app.showHoldings else "Hide Holdings")
    if app.sellStockNum is not None and app.sellAmount > 0:
        drawButton(app.sellButton, f"Sell {app.sellAmount}")

    # Show holdings if toggled
    if app.showHoldings:
        drawHorizontalPortfolio(app)


def sellStocks_onKeyPress(app, key):
    if len(app.playerPortfolio.stocks) == 0:
        if key == 'enter':
            setActiveScreen('stocks')
        return

    if key == 'c':
        app.sellStockNum = None
        app.sellAmount = 0
        return

    if key.isdigit():
        if app.sellStockNum is None:
            stockInd = int(key) - 1
            if 0 <= stockInd < len(app.playerPortfolio.stocks):
                app.sellStockNum = stockInd
        else:
            app.sellAmount = int(key)

    if key == 's' and app.sellStockNum is not None and app.sellAmount > 0:
        allStockTuples = list(app.playerPortfolio.stocks.keys())
        stockKey = allStockTuples[app.sellStockNum]
        stock = app.playerPortfolio.stocks[stockKey]
        if app.sellAmount <= stock['numHeld']:
            sellPrice = stock['newValue'] // stock['numHeld']
            revenue = math.ceil(sellPrice * app.sellAmount)
            app.player.money += revenue
            stock['numHeld'] -= app.sellAmount
            stock['oldValue'] = stock['numHeld'] * stockKey[0]
            if stock['numHeld'] == 0:
                app.playerPortfolio.stocks.pop(stockKey)
            app.log.insert(0, f"Made ${revenue} from Stocks")
            app.sellAmount = 0
            app.sellStockNum = None
            setActiveScreen('decision')
        else:
            print("Invalid number to sell.")

def sellStocks_onMousePress(app, mouseX, mouseY):
    if len(app.playerPortfolio.stocks) == 0:
        if pointInRect(mouseX, mouseY, app.returnToStocksButton):
            setActiveScreen('stocks')
        return

    if pointInRect(mouseX, mouseY, app.toggleHoldingsButton):
        app.showHoldings = not app.showHoldings

    elif pointInRect(mouseX, mouseY, app.sellButton):
        if app.sellStockNum is not None and app.sellAmount > 0:
            sellStocks_onKeyPress(app, 's')

def drawNothingToSell(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawLabel("Portfolio is empty.", app.width / 2, app.height / 2 - 30,
              fill='lime', bold=True, size=20, align='center')
    drawLabel("You can return to the stock market to buy.", app.width / 2, app.height / 2,
              fill='white', size=16, align='center')
    drawButton(app.returnToStocksButton, "Return to Stocks")

    
def drawHorizontalPortfolio(app):
    drawLabel("Your Holdings:", app.width // 2, 420, fill='lime', size=20, bold=True)
    spacingX = 240
    startY = 450
    wrapThreshold = app.width - 60
    x = 60
    y = startY

    for i, stock in enumerate(app.playerPortfolio.stocks):
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

def drawButton(rect, label):
    x, y, w, h = rect
    drawRect(x, y, w, h, fill='green', border='darkGreen', dashes= True, borderWidth=2)
    drawLabel(label, x + w // 2, y + h // 2, size=14, fill='lime', bold=True)

def pointInRect(x, y, rect):
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh
