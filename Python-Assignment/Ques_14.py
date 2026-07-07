# 14. Find the longest word in the string "Python programming is interesting".
def longest_word(text):
    words = text.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest Word :", longest)
    print("Length :", len(longest))

s = "Python programming is interesting"

longest_word(s)