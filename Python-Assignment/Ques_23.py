# 23. Print words in reverse order in "How are you sir" → "sir you are How".
def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

s = "How are you sir"

print("Original String :", s)
print("Reversed Words  :", reverse_words(s))