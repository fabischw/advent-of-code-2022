"""
Solution for
Day 1: Calorie Counting
"""


"""
rock: 1
paper: 2
scissors: 3
"""

player_choices = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}





with open("data.txt") as file:
    data = file.readlines()

for idx,lines in enumerate(data):
    data[idx] = lines.replace("\n","")


def part_one():


    combinations = {
        "A X": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
        "C Z": 3
    }

    total_score = 0
    for lines in data:
        score = combinations.get(lines) + player_choices.get(lines[2:])
        total_score += score
    print(total_score)



def part_two():
    #dictionaity to store what points the player gets when he needs to win
    win_table = {
        "A": 2,
        "B": 3,
        "C": 1
    }

    loose_table = {
        "A": 3,
        "B": 1,
        "C": 2
    }
    


    total_score = 0
    for lines in data:
        if lines[2:] == "X":#lose
            total_score += loose_table.get(lines[:1])
        elif lines[2:] == "Y":#draw
            total_score += 3 + player_choices.get(lines[:1])# 3 points for draw + amount of points for the character the opoonent has
        elif lines[2:] == "Z":#win
            total_score += 6 + win_table.get(lines[:1])# 6 points for winning + amount of points given for winning symbol -> use combinations dictionairy
    print(total_score)

