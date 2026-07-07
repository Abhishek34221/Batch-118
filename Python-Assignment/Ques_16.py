# 16. Remove all spaces from "How are you sir". 
def remove_spaces(text):
    return text.replace(" ", "")

s = "How are you sir"

print("Original String :", s)
print("Without Spaces  :", remove_spaces(s))