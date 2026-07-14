#10. Write a program to merge two dictionaries 
# d1 = {1: "a", 2: "b"} 
# d2 = {3: "c", 4: "d"}
def merge_dict(d1, d2):
    d1.update(d2)
    return d1

d1 = {1: "a", 2: "b"}
d2 = {3: "c", 4: "d"}

print(merge_dict(d1, d2))