import sys
from cmu_graphics import *

class Player:
    def __init__(self, name, age, money, moneyGoal):
        self.name = name
        self.age = age
        self.money = money
        self.moneyGoal = moneyGoal

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Money: ${self.money}"