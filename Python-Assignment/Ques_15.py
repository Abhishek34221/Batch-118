# 15. Capitalize the first letter of each word in "welcome to python world". 
def capitalize_words(text):
    return text.title()
s = "welcome to python world"

print("Original String :", s)
print("Capitalized String :", capitalize_words(s))