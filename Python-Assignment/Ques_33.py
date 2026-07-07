# 33. Find all occurrences of a substring in "This is Python and Python is fun" → Substring "Python". 
def find(text, sub):
    index = text.find(sub)

    while index != -1:
        print("Found at index:", index)
        index = text.find(sub, index + 1)

s = "This is Python and Python is fun"
substring = "Python"

find(s, substring)