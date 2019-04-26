from SolarSystem import SolarSystem
from TechLevel import TechLevel
from Resources import Resources
import random


class Universe:

    def __init__(self):
        self.solar_systems = []


        names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        for name in names:
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            coord = [x, y]
            self.solar_systems.append(SolarSystem(name, coord, random.choice(list(TechLevel)), random.choice(list(Resources))))



    def get_solar_systems(self):
        return self.solar_systems
