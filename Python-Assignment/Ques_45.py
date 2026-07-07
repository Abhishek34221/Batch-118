# 45. Find the longest common substring between two strings (e.g., "abcdxyz" and "xyzabcd" → Longest common substring = "abcd").
def longest_common_substring(str1, str2):
    longest = ""
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            sub = str1[i:j]

            if sub in str2 and len(sub) > len(longest):
                longest = sub

    return longest

s1 = "abcdxyz"
s2 = "xyzabcd"

print("Longest Common Substring:", longest_common_substring(s1, s2))