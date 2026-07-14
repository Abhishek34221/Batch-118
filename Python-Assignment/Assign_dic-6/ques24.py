# 24. Write a program to remove duplicate values from a dictionary. 
def remove_duplicate_values(data):
    result = {}
    seen = []
    for key, value in data.items():
        if value not in seen:
            seen.append(value)
            result[key] = value

    return result

d = {1: "a", 2: "b", 3: "a", 4: "c", 5: "b"}

print(remove_duplicate_values(d))