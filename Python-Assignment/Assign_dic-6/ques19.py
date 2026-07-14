# 19. Write a program to sort a dictionary by its keys d = {3: "three", 1: "one", 2: "two"} 
def sort_by_keys(data):
    sorted_dict = {}

    for key in sorted(data.keys()):
        sorted_dict[key] = data[key]

    return sorted_dict
d = {3: "three", 1: "one", 2: "two"}
print(sort_by_keys(d))