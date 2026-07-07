# 19. Swap cases of all letters in "Python Is Fun" → "pYTHON iS fUN".
def swap_cases(text):
    return text.swapcase()

s = "Python Is Fun"

print("Original String :", s)
print("Swapped String  :", swap_cases(s))