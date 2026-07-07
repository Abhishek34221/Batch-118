# 13. Count spaces, digits, alphabets, and special characters in "Python 3.9 is awesome!!".
def count_characters(text):
    spaces = 0
    digits = 0
    alphabets = 0
    special = 0

    for ch in text:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1

    print("Alphabets :", alphabets)
    print("Digits    :", digits)
    print("Spaces    :", spaces)
    print("Special Characters :", special)

s = "Python 3.9 is awesome!!"

count_characters(s)