# 8. Count the total occurrences of a specific letter in the string "this is python programming place".
def count_letter(string, letter):
    count = 0
    for ch in string:
        if ch == letter:
            count += 1
    return count

s = "this is python programming place"
letter = input("Enter a letter: ")

result = count_letter(s, letter)
print(f"'{letter}' occurs {result} times.")