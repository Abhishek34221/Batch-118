# 39. Split a string based on a substring (e.g., "apple,banana,grapes" → Split by "," → ["apple", "banana", "grapes"]). 
def split_string(text, separator):
    return text.split(separator)

s = "apple,banana,grapes"
separator = ","

print(split_string(s, separator))