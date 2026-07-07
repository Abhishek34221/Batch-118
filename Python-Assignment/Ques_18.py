# 18. Sort characters alphabetically in "programming" → "aggimmnoprr".
def sort_characters(text):
    result = "".join(sorted(text))
    return result

s = "programming"

print("Original String :", s)
print("Sorted String   :", sort_characters(s))