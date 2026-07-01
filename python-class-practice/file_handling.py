#----------- File handling
#1. File handling in python means reading from and writing to files/folder stored on
# disk using python.

#2. Your python code can open a file , pull out data of it , put data into it and 
# also close it properly.

#---------- What is file
# files are store of data and information on the specifi path of device.

# Types of file
# 1.Text file (.txt,.csv,.json)
# 2.Binary file (images,vedios,audio)

# Types of file path.
# 1.Absolute path : The complete path from the root of the filesystem.
# 2.Relative path : The path relative to where your current folder (current working dir)

# file mode
# 1. a : append , a+ : append and read
# 2. w : write , w+ : write and read
# 3. r : read  ,  r+ : read and write
# 4. x : strictly create file

# python file handling methods.
# 1.open(file_name,mode) : opens file 
# 2.close() : close file.
# 3.flush() : memory cleanup.

# 4.read() : file read.
# 5.readlines(): file read line by line.
# 6.write() : writes data in file only take string.
# 7.writelines() : write data in file of any data types.

# 8.tail(): cursor move
# 9.seek(): specific position set of cursor

# in-built modules
# os library
# shutil library
# subprocess libary
# random library
# string library

# -----------------------------------------------------
# 1.create a file in strict mode
# try:
#     file=open("demo.txt","x")
#     print("File Created")
# except Exception as e:
#     print("Error:",e)

# 2.write mode file creation
# file=open("new_demo.txt","w")
# file.write("This is file content using file handling")
# file.flush()
# file.close()
# print("file created in write mode..")

# import os
# print(os.getcwd())
# path=r"c:\Users\dev\OneDrive\Desktop"
# os.chdir(path)
# print(os.getcwd())

# file=open("data.py","w")
# file.write(f"print('File handling')")
# file.close()
# print(os.listdir())

# context manager.
# with open("manager.txt","w+") as file:
#     file.write("this is new content of file")
#     file.write("this is updated content")
#     file.seek(0)
#     r=file.read(4)
#     print("file written")
#     print(f"File content : {r}")

# with open("demo.txt", "r") as f:
#     print(f.read())
    

# count_digits=""
# total_char=0

# with open("demo.txt", "r") as file:
#     data = file.read()

# for i in data:
#     if i in "0123456789":
#         count_digits+=1
#     else:
#         total_char+=1
# with open('newfile.txt',"w") as file:
#     file.write(f"Total Digits in file : {count_digits}")
#     file.write("\n")
#     file.write(f"Total chars in file : {total_char}")



# with open("demo.txt", "r") as file:
#     data = file.read()
# result = ""

# for i in data:
#     if not i.isdigit():
#         result += i
# with open("newfile.txt", "w") as file:
#     file.write(result)

# print("Digits removed successfully.")


# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     res = num1/num2
# except Exception as e:
#     print("Please enter valid intiger.")
#     print("Cannot divided by zero")
# else:
#     print("Result: ",res)
# finally:
#     print("Program finised✅")


# n = int(input("Enter a number: "))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:

#     print("Prime")
# else:
#     print("Not Prime")




# emp_list=["aman","shivam","shubham","anshu","kamal"]
# # emp name individual file create txt type.
# for i in emp_list:
#     with open(f"{i}.txt", "w") as file:
#         data=file.write(i)
#         print("file created")


import os
# print(os.listdir())
# print("Current folder :",os.getcwd())
# path = "C:\\Users\Abhishek Singh\\OneDrive\\Desktop\\Python_practice"
# os.chdir(path)
# print("Current folder : ", os.getcwd())

emp_list=["aman","shivam","shubham","anshu","kamal"]

# for i in emp_list:
#     file_check=os.path.exists(f"{i}.txt")
#     if not file_check:
#         with open(f"{i}.txt","w") as file:
#             print(f"{i}.txt file is created✅")
#     else:
#         print(f"{i} - File allready exit")

# for i in emp_list:
#     os.remove(f"{i}.txt")
#     print(i, "Removed")

# var1=os.getcwd()
# print(var1)
# path=var1+"//"+var1
# os.chdir(path)


# folder = "Employee_Details"
# os.makedirs(folder)

# target = os.getcwd()+folder
# path=os.chdir(target)



# for i in emp_list:
#     with open(f"{i}.txt","w") as file:
#         print(i,"Created✅")












