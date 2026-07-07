# 42. Extract substring after a specific word (e.g., "Welcome to Python World" → substring after "to" → "Python World").
def substring_after_word(text, word):
    result = text.split(word)
    print(result[1].strip())

s = "Welcome to Python World"
substring_after_word(s, "to")