# 26. Convert a string into a list of words using "split()" (e.g., "Python is fun" → ["Python", "is", "fun"]). 
def string_to_list(text):
    return text.split()

s = "Python is fun"

result = string_to_list(s)

print(result)