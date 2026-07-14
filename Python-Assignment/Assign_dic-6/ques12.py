# 12. Write a program to find the minimum value in the dictionary marks = {"A": 85, "B": 90, "C": 75, "D": 95}
def minimum_value(marks):
    minimum = None

    for value in marks.values():
        if minimum is None or value < minimum:
            minimum = value

    print("Minimum Value:", minimum)

marks = {"A": 85, "B": 90, "C": 75, "D": 95}
minimum_value(marks)