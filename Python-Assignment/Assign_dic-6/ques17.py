# 17. Write a program to create a dictionary where keys are numbers from 1 to 5 and values are their squares. 
def create_square_dict():
    result = {}
    for i in range(1, 6):
        result[i] = i ** 2

    return result
print(create_square_dict())