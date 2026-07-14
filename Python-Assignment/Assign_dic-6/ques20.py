# 20. Write a program to count how many values are greater than 50 in a dictionary.
def count_values(data):
    count = 0
    for value in data.values():
        if value > 50:
            count += 1

    print("Count:", count)

d = {"A": 45, "B": 70, "C": 90, "D": 30, "E": 55}
count_values(d)