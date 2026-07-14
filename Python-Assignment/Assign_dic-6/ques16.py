# 16. Write a program to count the frequency of each character in a string using a dictionary. Example: "banana" 
def char_frequency(text):
    freq = {}

    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq
text = "banana"
print(char_frequency(text))