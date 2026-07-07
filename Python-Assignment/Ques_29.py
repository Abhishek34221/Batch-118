# 29. Check if two strings are anagrams (e.g., "listen" and "silent" → Anagrams).
def check_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        print("Anagrams")
    else:
        print("Not Anagrams")

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

check_anagram(s1, s2)