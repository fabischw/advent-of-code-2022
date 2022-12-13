"""
Solution for
Day 7: No Space Left On Device
"""

with open("data.txt") as file:
    data = file.readlines()

for idx,lines in enumerate(data):
    data[idx] = lines.replace("\n","")


def part_one():
    """
    approach:
    create a dictionairy with sub-dictionairies
    """

    file_structure = {}
    current_dirctory = ["/"]#saving the path to the current directory

    mode = "output"# variable to switch between output and user commands

    for instructions in data:
        if instructions.startswith("$"):
            cmd = instructions[2:]
            print(cmd)
            if cmd == "ls":
                mode = "output"
            elif cmd.startswith("cd"):
                # logic to switch to folder
                dest = cmd[3:]
                print(dest)

        #elif mode == "output":



#def part_two():


part_one()