# 17. Check if all characters in the string are unique (e.g., "abcde" → True, "hello" → False).
def unique_characters(text):
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]:
                return False
    return True

s = input("Enter a string: ")

print(unique_characters(s))