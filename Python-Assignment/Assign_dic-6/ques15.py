# 15. Write a program to remove a specific key (for example, key = 2) from the dictionary 
# d = {1: 10, 2: 20, 3: 30} 
def remove_key(data, key):
    data.pop(key, None)   # Removes the key if it exists
    return data

d = {1: 10, 2: 20, 3: 30}
print(remove_key(d, 2))