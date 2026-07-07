# 24. Count words in the string "This is a python assignment".
def count_words(text):
    words = text.split()
    return len(words)

s = "This is a python assignment"

print("Total Words:", count_words(s))