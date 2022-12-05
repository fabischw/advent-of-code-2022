"""
Solution for
Day 5: Supply Stacks
"""

with open("data.txt") as file:
    data = file.readlines()

for idx,lines in enumerate(data):
    data[idx] = lines.replace("\n","")

instructions = data[10:]


stacks = {
    "stack1": [],
    "stack2": [],
    "stack3": [],
    "stack4": [],
    "stack5": [],
    "stack6": [],
    "stack7": [],
    "stack8": [],
    "stack9": []
}



for i in range(1,10):
    stack = f"stack{i}"
    for n in range(0,8):# 1, 8 for data
        if data[n][1+(i-1)*4] != " ":
            stacks[stack].append(data[n][1+(i-1)*4])


for i in range(1,10):
    stacks[f"stack{i}"].reverse()


def part_one():
    for lines in instructions:
        count = int(lines[lines.find("move ")+5:lines.find(" from")])
        origin = int(lines[lines.find("from ")+5:lines.find(" to")])
        dest = int(lines[lines.find("to ")+3:])

        for i in range(0,count):
            stack_origin = f"stack{origin}"
            stack_dest = f"stack{dest}"
            crate = stacks[stack_origin].pop()

            stacks[stack_dest].append(crate)

    for keys, elements in stacks.items():
        print(elements)



def part_two():
    for lines in instructions:
        count = int(lines[lines.find("move ")+5:lines.find(" from")])
        origin = int(lines[lines.find("from ")+5:lines.find(" to")])
        dest = int(lines[lines.find("to ")+3:])

        #create a stack with items that have to be moved in order
        movestack = []
        for i in range(0,count):
            movestack.append(stacks[f"stack{origin}"].pop())

        for i in range(0,len(movestack)):
            stacks[f"stack{dest}"].append(movestack[len(movestack)-i-1])


    for keys, elements in stacks.items():
        print(elements)