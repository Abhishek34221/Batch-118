# 22. Check if a substring exists in "Python programming" (e.g., "thon" → Found).
def check_substring(text, sub):
    if sub in text:
        print("Found")
    else:
        print("Not Found")

s = "Python programming"
substring = input("Enter substring: ")

check_substring(s, substring)