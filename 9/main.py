"""
Solution for
Day 9: Rope Bridge
"""
from copy import deepcopy


with open("data.txt") as file:
    data = file.readlines()

for idx,lines in enumerate(data):
    data[idx] = lines.replace("\n","")


def does_touch(current_grid: list, head: list, tail: list):
    """
    function that checks if the head and tail touch:
    current_grid: array of arrays of arrays (main array contains 5 row arrays containing the row data)
    head: indexes of the set indexes, ex: [2,3] note that the first index is always 0
    tail: indexes of the set indexes, ex: [2,4] note that the first index is always 0
    """




def part_one():

    layout = [["." for i in range(0,6)] for i in range(0, 5)]# creating one array containing the grid:
    # each array represents another row of the grid

    layout[4][0] = "s"# setting the starting point

    visit_map = layout.deepcopy()#creating a seperate grid to store the tail locations

    # debug statement
    for elements in layout:
        print(elements)


    current_head_pos = []# creating an array to save the current head position

    for chars in data:
        direction = chars[:1]
        step_count = int(chars[1:])

        if direction == "L":
            """
            model left movement
            """

        elif direction == "R":
            """
            model right movement
            """

        elif direction == "U":
            """
            model up movement
            """

        elif direction   == "D":
            """
            model down movement
            """

        #print(direction, step_count)



part_one()
