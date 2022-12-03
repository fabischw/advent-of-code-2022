"""
Solution for
Day 3: Rucksack Reorganization
"""

with open("data.txt") as file:
    data = file.readlines()

for idx,lines in enumerate(data):
    data[idx] = lines.replace("\n","")


    def prioritize_chars(char):
        if char.lower() == char:
            return ord(char) - 96
        elif char.upper() == char:
            return ord(char) - 64 + 26



def part_one():
    totalchars = ""
    total_value = 0


    def find_same_letter(half1,half2):
        for chars_prio in half1:
            for chars in half2:
                if chars_prio == chars:
                    return chars




    for lines in data:
        mid = len(lines) // 2
        first = lines[mid:]
        last = lines[:mid]

        totalchars += find_same_letter(first, last)


    for chars in totalchars:
        total_value += prioritize_chars(chars)

    print(total_value)



def part_two():

    total_value = 0
    badges = ""

    groups = []
    temparr = []

    for idx, lines in enumerate(data):
        temparr.append(lines)
        if (idx+1) % 3 == 0:
            groups.append(temparr)
            temparr = []


    def find_same_letter(substr1,substr2,substr3):
        for chars1 in substr1:
            for chars2 in substr2:
                for chars3 in substr3:
                    if chars1 == chars2 == chars3:
                        return chars1



    for backpacks in groups:
        badges += find_same_letter(backpacks[0],backpacks[1],backpacks[2])

    for chars in badges:
        total_value += prioritize_chars(chars)

    print(total_value)

