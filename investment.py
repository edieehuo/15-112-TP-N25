# import sys
# from cmu_graphics import *
# from buyStocks import *
# from sellStocks import *

# #--------INVESTMENT INFO SCREEN--------------------------------- 
# def investment_onScreenActivate(app):
#     app.screenName = 'investment'
#     pass
    
# def investment_redrawAll(app):
#     drawLabel("Investment Screen", app.width/2, 10, size=40, bold=True)
#     drawLabel("Press S for Stocks", app.width/2, app.height/2 - 50)

# def investment_onKeyPress(app, key):
#     if key == 's':
#         app.screenName = 'stocks'
#         setActiveScreen('stocks')
#     else:
#         pass  # Ignore other keys