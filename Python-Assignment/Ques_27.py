# 27. Join a list of words into a string using "join()" (e.g., ["Python", "is", "fun"] → "Python is fun"). 
def join_words(words):
    return " ".join(words)

word_list = ["Python", "is", "fun"]
result = join_words(word_list)
print(result)