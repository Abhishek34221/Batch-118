# 25. Write a program to check whether all values in a dictionary are unique.
def check_unique_values(data):
    values = list(data.values())

    if len(values) == len(set(values)):
        print("All values are unique.")
    else:
        print("Duplicate values found.")

d = {1: "a", 2: "b", 3: "c", 4: "d"}
check_unique_values(d)