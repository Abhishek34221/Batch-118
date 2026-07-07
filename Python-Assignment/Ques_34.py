# 34. Replace a substring in "I like Python" → Replace "Python" with "Java".
def replace_substring(text):
    return text.replace("Python", "Java")

s = "I like Python"

print("Original String :", s)
print("Modified String :", replace_substring(s))