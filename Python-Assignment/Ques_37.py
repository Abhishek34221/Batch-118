# 37. Check if a string starts with a substring (e.g., "Python is easy" starts with "Python").
def starts_with(text, sub):
    if text.startswith(sub):
        print("Starts with", sub)
    else:
        print("Does not start with", sub)

s = "Python is easy"
substring = "Python"

starts_with(s, substring)