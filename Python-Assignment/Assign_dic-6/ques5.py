# 5. Write a program to calculate the total score of all students student_score = {1: 44, 2: 45, 3: 55}
def total_score(student_score):
    total = 0
    for score in student_score.values():
        total += score

    return total
student_score = {1: 44, 2: 45, 3: 55}
print("Total Score:", total_score(student_score))