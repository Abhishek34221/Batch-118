# 9. Write a program to find all values that start with the letter ‘K’ player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"} 
def values_start_with_k(player):
    for value in player.values():
        if value.startswith("K"):
            print(value)

player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}

values_start_with_k(player)