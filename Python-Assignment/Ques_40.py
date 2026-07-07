# 40. Find the index of the first occurrence of a substring in "Programming is great" → Substring "is" → Index 12.
def find_index(text, sub):
    index = text.find(sub)

    if index != -1:
        print("Index:", index)
    else:
        print("Substring not found")

s = "Programming is great"
substring = "is"

find_index(s, substring) 