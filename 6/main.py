"""
Solution for
Day 6: Tuning Trouble
"""

with open("data.txt") as file:
    data = file.readlines()

for idx,lines in enumerate(data):
    data[idx] = lines.replace("\n","")

data = str(data[0])


def part_one():
    for i in range(0,len(data)-1):
        if len(set(data[i:i+4])) == 4:
            print(set(data[i:i+4]),i+4)
            return


def part_two():
    for i in range(0,len(data)-1):
        if len(set(data[i:i+14])) == 14:
            print(set(data[i:i+14]),i+14)
            return

