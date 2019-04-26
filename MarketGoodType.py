from enum import Enum


class MarketGoodType(Enum):
    water = ["Water", 30, 4, 3]
    furs = ["Furs", 250, 10, 10]

    def __init__(self, name, base_price, var, ipl):
        self.name = name
        self.base_price = base_price
        self.var = var
        self.ipl = ipl

    def can_buy(self):


