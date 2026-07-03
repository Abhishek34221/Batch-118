import json
import pymysql

# from faker import Faker

# fake = Faker("en_IN")

# students = []

# for i in range(1, 26):  
#     student = {
#         "id": i,
#         "name": fake.first_name(),
#         "role": fake.random_number(digits=5),
#         "age": fake.random_int(min=18, max=30),
#         "email": fake.email(),
#         "phone": fake.msisdn()[:10]
#     }

#     students.append(student)

# data = {
#     "students": students
# }

# with open("student_profile.json", "w") as file:
#     json.dump(data, file, indent=4)

# print("Created successfully ")


with open("student_profile.json", "r") as file:
    student_data = json.load(file)

students = student_data["students"]

DATABASE = "student_db"
TABLE = "students"


conn = pymysql.connect(host="localhost",user="root",password="abhi@123")

cursor = conn.cursor()


cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
cursor.execute(f"USE {DATABASE}")

print("Database Ready ")


cursor.execute(f"DROP TABLE IF EXISTS {TABLE}")


first_student = students[0]

columns = []

for key, value in first_student.items():

    if key == "id":
        columns.append(f"{key} INT PRIMARY KEY")

    elif isinstance(value, int):
        columns.append(f"{key} INT")

    else:
        columns.append(f"{key} VARCHAR(255)")

create_query = f"""
CREATE TABLE {TABLE}({", ".join(columns)})
"""

cursor.execute(create_query)

print("Table Created Successfully")

column_names = list(first_student.keys())

placeholders = ", ".join(["%s"] * len(column_names))

insert_query = f"""
INSERT INTO {TABLE}
({", ".join(column_names)})
VALUES ({placeholders})
"""

for student in students:

    values = tuple(student[col] for col in column_names)

    cursor.execute(insert_query, values)

conn.commit()

print("Data Inserted Successfully")


cursor.execute(f"SELECT * FROM {TABLE}")

rows = cursor.fetchall()

print("\nStudent Records\n")

for row in rows:
    print(row)

cursor.close()
conn.close()