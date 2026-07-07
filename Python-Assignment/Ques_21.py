# 21. Remove vowels from "How are you sir" → "Hw r y sr".
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch

    return result
s = "How are you sir"

print("Original String :", s)
print("After Removing Vowels :", remove_vowels(s))