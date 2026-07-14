# 1. Write a program to calculate the sum of all keys in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4} 
def sum_keys(dictionary):
    total = 0
    for key in dictionary:
        total += key

    return total

d = {1: 1, 2: 2, 3: 3, 4: 4}
print("Sum of Keys:", sum_keys(d))