# 20. Find frequency of each character in "banana" → { 'b':1, 'a':3, 'n':2 }.
def character_frequency(text):
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

s = "banana"

print(character_frequency(s))