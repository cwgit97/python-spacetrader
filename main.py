from Player import Player
from Universe import Universe

skills = dict.fromkeys(["PILOT", "FIGHTER", "TRADER", "ENGINEER"])
skills = dict.fromkeys(skills.keys(), 0)
difficulty = None
difficulty_list = ["BEGINNER", "EASY", "NORMAL", "HARD", "IMPOSSIBLE"]


def allocate_points():
    global skills
    while sum(skills.values()) != 16:

        error = False
        for skill in skills:
            try:
                num_points = int(input("Enter points for skill " + skill + ": "))
            except ValueError:
                print("ERROR: Invalid input")
                error = True
                break;
            if num_points < 0:
                print("ERROR: Cannot assign negative points")
                error = True
                break
            else:
                skills[skill] = num_points

        if sum(skills.values()) != 16 and error is False:
            print("ERROR: Must assign exactly 16 points")
            skills = dict.fromkeys(skills.keys(), 0)


def choose_difficulty():
    global difficulty
    while difficulty not in difficulty_list:
        print(difficulty_list)
        difficulty = input(("Choose a difficulty: ")).upper()
        if difficulty not in difficulty_list:
            print("Invalid difficulty chosen")









print("SPACE TRADER \n")

input_name = input("Enter your name: ")

print("NAME: " + input_name)


allocate_points()

choose_difficulty()

test_player = Player(input_name, skills, difficulty)

print(test_player.get_name())
print(test_player.get_skills())
print(test_player.get_difficulty())
print(test_player.get_credits())
print(test_player.get_ship_type())

test_universe = Universe()

for solar in  test_universe.get_solar_systems():
    print(solar.get_name())
    print(solar.get_coords())
    print(solar.get_tech_level())
    print(solar.get_resources())


print("END")