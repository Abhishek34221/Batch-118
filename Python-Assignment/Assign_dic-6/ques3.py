# 3. Write a program to calculate the sum of both keys and values in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4}
def sum_keys_values(dictionary):
    total = 0
    for key, value in dictionary.items():
        total += key + value

    return total

d = {1: 1, 2: 2, 3: 3, 4: 4}
print("Sum of Keys and Values:", sum_keys_values(d))