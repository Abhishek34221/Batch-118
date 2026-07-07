# 10. Print alternate letters from the string "How are you sir".
def alternate_letters(text):
    for i in range(0, len(text), 2):
        print(text[i], end="")
s = "How are you sir"
alternate_letters(s)