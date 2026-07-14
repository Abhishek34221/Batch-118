# 18. Write a program to find the total number of items in the dictionary d = {"apple": 5, "banana": 7, "cherry": 3} 
def total_items(data):
    count = 0

    for key in data:
        count += 1

    print("Total Items:", count)
d = {"apple": 5, "banana": 7, "cherry": 3}
total_items(d)