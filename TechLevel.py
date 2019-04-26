from enum import Enum


class TechLevel(Enum):

    PRE_AGRICULTURE = 0
    AGRICULTURE = 1
    MEDIEVAL = 2
    RENAISSANCE = 3
    EARLY_INDUSTRIAL = 4
    INDUSTRIAL = 5
    POST_INDUSTRIAL = 6
    HI_TECH = 7

    def get_index(self, tech_level):
        return TechLevel.value