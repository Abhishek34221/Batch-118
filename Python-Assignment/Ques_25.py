# 25. Find the ASCII value of each character in "ABcd".
def ascii_values(text):
    for i in text:
        print(i, "=", ord(i))

s = "ABcd"

ascii_values(s)