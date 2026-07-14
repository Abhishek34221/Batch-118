# 11. Write a program to check whether a given key exists in the dictionary d = {1: 100, 2: 200, 3: 300}
def check_key(dictionary, key):
    if key in dictionary:
        print("Key exists")
    else:
        print("Key does not exist")

d = {1: 100, 2: 200, 3: 300}

key = int(input("Enter key: "))

check_key(d, key)