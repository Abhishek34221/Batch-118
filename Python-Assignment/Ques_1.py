#1. Filter vowels and consonants from the string "How are you sir".
def filter_vowl_consonant(res):
    vowels = ""
    consonants = ""
    for i in res:
        if i.isalpha():
            if i in "aeiou":
                vowels += i
            else:
                consonants += i
    print("Vowels :", vowels)
    print("Consonants :", consonants)


res = "How are you sir"
filter_vowl_consonant(res)
