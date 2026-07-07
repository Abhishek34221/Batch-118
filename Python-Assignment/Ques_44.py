# 44. Check if two strings are rotations (cyclic substrings) of each other (e.g., "abcd" and "cdab" → Rotations). 
def check_rotation(str1, str2):
    if len(str1) == len(str2) and str2 in (str1 + str1):
        print("Rotations")
    else:
        print("Not Rotations")

s1 = "abcd"
s2 = "cdab"

check_rotation(s1, s2)