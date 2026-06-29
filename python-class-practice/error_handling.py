try:
    a=20
    b=2
    c=a/b
    print(c)
except Exception as e:
    print("Error",e)

finally:
    print("i always run...")


# ZeroDivisionError: Dividion by zero
# nameError : name 'w' is not defined
# TypeError: unsupported oprend types(s) /: 'int' 