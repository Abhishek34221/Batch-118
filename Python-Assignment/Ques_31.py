# 31. Extract a substring from "Python Programming" → from index 0 to 6 should give "Python".
def extract_substring(text, start, end):
    return text[start:end]

s = "Python Programming"

result = extract_substring(s, 0, 6)

print("Substring:", result) 