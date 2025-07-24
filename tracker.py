import sys
from cmu_graphics import *
#--- Tracker Screen --------------------------------------------------------------------------------------
'''Draw on every screen while game is active to show player info, time left, and money.'''
def tracker_onScreenActivate(app):
    app.left = 0
    app.right = app.width
    app.top = 0
    app.bottom = app.height
    app.border = 20  
    pass 

def tracker_redrawAll(app):
    drawLabel(f"Player: {app.player.name}", app.left + app.border, app.top + 20, size=20, align = 'left')
    drawLabel(f"Your Savings: ${app.player.money},000", app.left + app.border, app.top + 50, size=20, align = 'left')
    drawLabel(f"Your Goal: ${app.player.moneyGoals},000 ", app.left + app.border, app.top + 80, size=20, align = 'left')
    drawLabel(f"Years Left: {app.time - app.currDec} ", app.left + app.border, app.top + 100, size=20, align = 'left')
    pass
