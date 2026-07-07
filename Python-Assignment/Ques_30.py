# 30. Replace all spaces with hyphens (-) in "Python is easy to learn" → "Python-is-easy-to-learn".
def replace_spaces(text):
    return text.replace(" ", "-")

s = "Python is easy to learn"

print("Original String :", s)
print("Modified String :", replace_spaces(s))