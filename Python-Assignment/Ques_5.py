# 5. Remove duplicate letters from the string "this is python programming place".
def remove_duplicate(res):
    result = ""
    for i in res:
        if i not in result:
            result += i
    print("Removing Duplicates:", result)
res = "this is python programming place"
remove_duplicate(res)
