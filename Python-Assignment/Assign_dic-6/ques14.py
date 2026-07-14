# 14. Write a program to swap keys and values in the dictionary d = {1: "one", 2: "two", 3: "three"}
def swap_keys_values(data):
    swapped = {}

    for key, value in data.items():
        swapped[value] = key

    return swapped
d = {1: "one", 2: "two", 3: "three"}
print(swap_keys_values(d))