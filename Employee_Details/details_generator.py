import os


# emp_list=["aman","shivam","shubham","anshu","kamal"]

# for i in emp_list:
#     file_check=os.path.exists(f"{i}.txt")
#     if not file_check:
#         with open(f"{i}.txt","w") as file:
#             print(f"{i}.txt file is created✅")
#     else:
#         print(f"{i} - File allready exit")

import os

path = r"C:\Users\Abhishek Singh\OneDrive\Desktop\Python_practice\Employee_Details"
os.chdir(path)
print(os.getcwd())
# print(os.getcwd())
# emp_list=["aman","shivam","shubham","anshu","kamal"]
# for i in emp_list:
#     file_check=os.path.exists(f"{i}.txt")
#     if not file_check:
#         with open(f"{i}.txt","w") as file:
#             print(f"{i}.txt file is created✅")
#     else:
#         print(f"{i} - File allready exit")


import random
import string
ID="".join([random.choice(string.digits+string.ascii_uppercase) for i in range(9)])
meeting_id="".join([random.choice(string.digits+string.ascii_uppercase) for i in range(25)])

def create_details(files):
    for i in files:
        if ".txt" in i:
            print(f"Files : {i}")
    select=input("Select your file without ext : ")
    with open(f"{select}.txt","w") as file:
        file.write(f"Name : {select}"+"\n")
        file.write(f"CANDIDATE_ID : {ID}"+"\n")
        file.write(f"MEETING_ID : http://{meeting_id}"+"\n")
        file.write(f"CANDIDATE_EMAIL : {input("Enter Your Email : ")}"+"\n")

    print(f"{select} file updated...")
files=os.listdir()
create_details(files)

