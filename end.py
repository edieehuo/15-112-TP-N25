from cmu_graphics import *

#---End Screen--------------------------------------------------------------------------------------
def end_onScreenActivate(app):
    pass

def end_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')  # Background

    titleY = 80
    drawLabel("Game Over", app.width // 2, titleY, size=48, fill='lime', bold=True)

    # Money Summary
    msgY = titleY + 60
    goalMet = app.player.money >= app.player.moneyGoals

    if goalMet:
        drawLabel(f"Goal Reached!", app.width // 2, msgY, size=28, fill='lightGreen', bold=True)
    else:
        drawLabel("You didn't reach your goal.", app.width // 2, msgY, size=28, fill='red', bold=True)

    # Bar Chart Summary
    barY = msgY + 60
    barW, barH = 500, 30
    barX = app.width // 2 - barW // 2
    drawRect(barX, barY, barW, barH, fill='dimGrey', border='white')

    percent = app.player.money / app.player.moneyGoals
    percent = min(max(percent, 0), 1)
    fillColor = 'lightGreen' if goalMet else 'orange'
    drawRect(barX, barY, barW * percent, barH, fill=fillColor)

    drawLabel(f"${app.player.money} / ${app.player.moneyGoals}", 
              app.width // 2, barY + barH + 25, 
              fill='white', size=16, bold=True)

    # Final Message
    drawLabel(f"You earned a total of ${app.player.money}.", 
              app.width // 2, barY + barH + 70, 
              fill='white', size=20)

    drawLabel("Press 'Enter' to Restart", 
              app.width // 2, app.height - 80, 
              size=20, fill='yellow', bold=True)

def end_onKeyPress(app, key):
    if key == 'enter':
        setActiveScreen('start')  # Restart the game
