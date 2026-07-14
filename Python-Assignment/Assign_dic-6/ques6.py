# 6. Write a program to separate odd and even keys from a dictionary. Also count the total number of odd keys and even keys.
def separate_keys(data):
    odd_keys = []
    even_keys = []

    for key in data:
        if key % 2 == 0:
            even_keys.append(key)
        else:
            odd_keys.append(key)

    print("Odd Keys :", odd_keys)
    print("Even Keys:", even_keys)
    print("Total Odd Keys :", len(odd_keys))
    print("Total Even Keys:", len(even_keys))

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

separate_keys(d)