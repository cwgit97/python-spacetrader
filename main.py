from Player import Player

skills = dict.fromkeys(["PILOT", "FIGHTER", "TRADER", "ENGINEER"])
skills = dict.fromkeys(skills.keys(), 0)
difficulty = None
difficulty_list = ["BEGINNER", "EASY", "NORMAL", "HARD", "IMPOSSIBLE"]


def allocate_points():
    global skills
    while sum(skills.values()) != 16:

        for skill in skills:
            num_points = int(input("Enter points for skill " + skill + ": "))
            if num_points < 0:
                print("ERROR: Cannot assign negative points")
                break
            else:
                skills[skill] = num_points

        if sum(skills.values()) != 16:
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

print(test_player.get_skills())


print("END")