# 41. Find the index of the last occurrence of a substring in "Programming in Python Programming" → Substring "Programming". 
def last_index(text, sub):
    index = text.rfind(sub)

    if index != -1:
        print("Last Index:", index)
    else:
        print("Substring not found")

s = "Programming in Python Programming"
substring = "Programming"

last_index(s, substring)