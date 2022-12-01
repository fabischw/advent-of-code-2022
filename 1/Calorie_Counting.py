"""
Solution for
Day 1: Calorie Counting
"""



with open("data.txt") as file:
    data = file.readlines()


def create_sum_arr():
    temparr = []
    current_sum = 0
    for elements in data:
        if elements != "\n":
            current_sum += int(elements.replace("\n",""))
        else:
            temparr.append(current_sum)
            current_sum = 0
    temparr.append(current_sum)
    temparr.sort(reverse=True)
    return temparr

data_sorted = create_sum_arr()




print(data_sorted[0], sum(data_sorted[:3]))