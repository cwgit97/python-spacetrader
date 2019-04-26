

class Player:

    def __init__(self, name, skills, difficulty):
        self.name = name
        self.skills = skills
        self.difficulty = difficulty
        self.credits = 1000
        self.ship_type = "GNAT"

    def get_name(self):
        return self.name

    def get_skills(self):
        return self.skills

    def get_difficulty(self):
        return self.difficulty

    def get_credits(self):
        return self.credits

    def get_ship_type(self):
        return self.ship_type