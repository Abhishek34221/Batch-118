# 11. Convert the string "qwertyuiopasdfghjklzxcvbnm" to "abcdefghijklmnopqrstuvwxyz". 
def convert_string(text):
    original = "qwertyuiopasdfghjklzxcvbnm"
    target = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for ch in text:
        index = original.index(ch)
        result += target[index]

    return result
s = "qwertyuiopasdfghjklzxcvbnm"

print("Original :", s)
print("Converted:", convert_string(s))
