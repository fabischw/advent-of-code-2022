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

    file_structure = {
        "/": None
    }
    cwd = ["/"]#saving the path to the current directory

    mode = "output"# variable to switch between output and user commands

    for instructions in data:
        if instructions.startswith("$"):#checking if the line is a command
            cmd = instructions[2:]#current command
            if cmd == "ls":
                mode = "output"#changing the mode to output -> setting up 'listener' 
            elif cmd.startswith("cd"):
                # logic to switch to folder
                dest = cmd[3:]
                #getting to the previous subfolder
                if dest == ".."and len(cwd) > 1:
                    cwd.pop()
                mode = "cmd"


        elif mode == "output":
            if instructions.startswith("dir"):
                dirname = instructions[4:]#getting the name for the new directory


                #getting to the current working directory
                current = file_structure.get("/")# entry point for the loop below
                for elements in cwd:
                    current = current.get(str(elements))
                
                
                current[dirname] = {}#setting the new directory as a key in the dict


#def part_two():


part_one()
