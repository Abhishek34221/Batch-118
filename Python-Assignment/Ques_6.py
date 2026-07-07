# 6. Search for a specific character in the string "this is python programming place".
def search(res, char):
    find = False
    for i in res:
        if i == char:
            find = True
            break
    if find:
        print(f"'{char}' is present in the string.")
    else:
        print(f"'{char}' is not present in the string.")

res = "this is python programming place"
character = input("Enter character to search: ")
search(res, character)