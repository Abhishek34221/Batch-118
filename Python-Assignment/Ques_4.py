# 4. Convert lowercase letters to uppercase in the string "How are you sir".
def convert(res):
    result = ""
    for i in res:
        result += i.upper()
    print("Uppercase String:", result)
res = "How are you sir"
convert(res)