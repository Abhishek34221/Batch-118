# 28. Find the first non-repeating character in "swiss" → "w".
def first_non_repeating(text):
    for i in text:
        if text.count(i) == 1:
            return i
    return "No non-repeating character"

s = "swiss"
print("First Non-Repeating Character:", first_non_repeating(s))