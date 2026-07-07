# 43. Extract substring before a specific word (e.g., "Welcome to Python World" → substring before "Python" → "Welcome to").
def substring_before_word(text, word):
    result = text.split(word)
    print(result[0].strip())

s = "Welcome to Python World"

substring_before_word(s, "Python")