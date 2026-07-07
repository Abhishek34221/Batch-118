# 32. Check if one string is a substring of another (e.g., "gram" is a substring of "Programming").
def check_substring(main_string, sub_string):
    if sub_string in main_string:
        print("Substring Found")
    else:
        print("Substring Not Found")

main = "Programming"
sub = "gram"
check_substring(main, sub) 