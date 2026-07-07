# 35. Remove a substring from "HelloWorld" → Remove "World" → "Hello". 
def remove_substring(text):
    return text.replace("World", "")

s = "HelloWorld"

print("Original String :", s)
print("Modified String :", remove_substring(s))