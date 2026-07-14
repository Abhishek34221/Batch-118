# 23. Write a program to convert two lists into a dictionary Example: keys = [1, 2, 3], values = ["a", "b", "c"] 
def create_dictionary(keys, values):
    result = dict(zip(keys, values))
    return result
keys = [1, 2, 3]
values = ["a", "b", "c"]

print(create_dictionary(keys, values))