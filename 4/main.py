"""
Solution for
Day 4: Camp Cleanup
"""

with open("data.txt") as file:
    data = file.readlines()

for idx,lines in enumerate(data):
    data[idx] = lines.replace("\n","")


def check_contain_full(range1_min, range1_max, range2_min, range2_max):
    return range1_min <= range2_min <= range2_max <= range1_max or range2_min <= range1_min <= range1_max <= range2_max

def check_contain_partial(range1_min, range1_max, range2_min, range2_max):
    return range1_min <= range2_min <= range1_max  or range2_min <= range1_min <= range2_max




def part_one():
    count = 0

    for lines in data:

        #splitting the data into 2 parts (elf1, elf2)

        elf1,elf2 = lines.split(sep=",")
        elf1_min, elf1_max = elf1.split("-")
        elf2_min, elf2_max = elf2.split("-")

        elf1_min = int(elf1_min)
        elf1_max = int(elf1_max)
        elf2_min = int(elf2_min)
        elf2_max = int(elf2_max)


        if check_contain_full(elf1_min,elf1_max,elf2_min,elf2_max):
            count += 1



    print(count)


def part_two():
    count = 0

    for lines in data:

        #splitting the data into 2 parts (elf1, elf2)

        elf1,elf2 = lines.split(sep=",")
        elf1_min, elf1_max = elf1.split("-")
        elf2_min, elf2_max = elf2.split("-")

        elf1_min = int(elf1_min)
        elf1_max = int(elf1_max)
        elf2_min = int(elf2_min)
        elf2_max = int(elf2_max)


        if check_contain_partial(elf1_min,elf1_max,elf2_min,elf2_max):
            count += 1

    print(count)
