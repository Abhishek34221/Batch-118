# 3. Reverse the string "How are you sir".
def reverse_string(res):
    reverse = ""
    for i in res:
        reverse = i + reverse
    print("Reversed String :", reverse)
res = "How are you sir"
reverse_string(res)