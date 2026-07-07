# 9. Replace "python" with "javascript" in the string "python developer python engineer python holder".
def replace_word(text):
    new_text = text.replace("python", "javascript")
    return new_text

s = "python developer python engineer python holder"
result = replace_word(s)
print("Original String:")
print(s)

print("Modified String:")
print(result)