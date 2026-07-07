# 12. Check if the string is a palindrome (e.g., "madam" → Palindrome, "hello" → Not palindrome).
def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

s = input("Enter a string: ")
palindrome(s)