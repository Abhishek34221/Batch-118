# 13. Write a program to find the maximum value in the dictionary marks = {"A": 85, "B": 90, "C": 75, "D": 95} 
def maximum_value(marks):
    maximum = None

    for value in marks.values():
        if maximum is None or value > maximum:
            maximum = value
    print("Maximum Value:", maximum)

marks = {"A": 85, "B": 90, "C": 75, "D": 95}
maximum_value(marks)