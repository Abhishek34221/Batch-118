# 22. Write a program to update a value in a dictionary if the key exists; otherwise, add the key.
def update_or_add(data, key, value):
    if key in data:
        data[key] = value
        print("Key updated.")
    else:
        data[key] = value
        print("Key added.")

    print(data)

d = {"A": 45, "B": 70, "C": 90}
update_or_add(d, "B", 80)
update_or_add(d, "D", 60)