# 21. Write a program to find the key with the highest value in a dictionary. 
def highest_value_key(data):
    max_key = None
    max_value = None

    for key, value in data.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key

    print("Key with Highest Value:", max_key)
    print("Highest Value:", max_value)

d = {"A": 45, "B": 70, "C": 90, "D": 30}

highest_value_key(d)