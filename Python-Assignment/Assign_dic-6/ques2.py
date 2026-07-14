# 2. Write a program to calculate the sum of all values in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4} 
def sum_values(dictionary):
    total = 0
    for value in dictionary.values():
        total += value

    return total
d = {1: 1, 2: 2, 3: 3, 4: 4}
print("Sum of Values:", sum_values(d))