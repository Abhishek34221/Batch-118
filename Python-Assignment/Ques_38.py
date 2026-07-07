# 38. Check if a string ends with a substring (e.g., "Learn coding" ends with "coding"). 
def ends_with(text, sub):
    if text.endswith(sub):
        print("Ends with", sub)
    else:
        print("Does not end with", sub)

s = "Learn coding"
substring = "coding"

ends_with(s, substring)