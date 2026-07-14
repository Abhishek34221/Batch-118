# 8. Write a program to extract alternate key-value pairs from the dictionary player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
def alternate_pairs(player):
    items = list(player.items())

    for i in range(0, len(items), 2):
        print(items[i])

player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}

alternate_pairs(player)