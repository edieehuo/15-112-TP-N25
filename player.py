import sys
from cmu_graphics import *

class Player:
    def __init__(self, name, money, moneyGoals, time):
        self.name = name
        self.money = money
        self.moneyGoals = moneyGoals
        self.time = time 

    def __repr__(self):
        return f"PlayerName: {self.name}, PlayerMoney: ${self.money}, PlayerMoneyGoals: ${self.moneyGoals}, PlayerTime: {self.time} years"