# 7. Write a program to find the greatest key in the dictionary player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
def greatest_key(player):
    greatest = None

    for key in player:
        if greatest is None or key > greatest:
            greatest = key

    print("Greatest Key:", greatest)
    print("Value:", player[greatest])

player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}

greatest_key(player)