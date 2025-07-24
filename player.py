import sys
from cmu_graphics import *

class Player:
    def __init__(self, name, money, moneyGoal, time):
        self.name = name
        self.money = money
        self.moneyGoal = moneyGoal
        self.time = time 

    def __repr__(self):
        return f"PlayerName: {self.name}, PlayerMoney: ${self.money}, PlayerMoneyGoal: ${self.moneyGoal}, PlayerTime: {self.time} years"