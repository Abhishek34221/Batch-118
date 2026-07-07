#2. Count vowels and consonants in the string "How are you sir".
def count_vowel_consonant(res):
    vowel_count = 0
    consonant_count = 0
    for i in res:
        if i != " ":   
            if i in "aeiou":
                vowel_count += 1
            else:
                consonant_count += 1
    print("Total vowels:", vowel_count)
    print("Total Consonants:", consonant_count)
res = "How are you sir"
count_vowel_consonant(res)