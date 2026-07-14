# 4. Create an empty dictionary called user_data. Allow the user to enter key-value pairs until they choose to stop. Print the final dictionary. 
def create_dictionary():
    user_data = {}
    while True:
        key = input("Enter key: ")
        value = input("Enter value: ")

        user_data[key] = value

        choice = input("Do you want to add more? (yes/no): ").lower()

        if choice == "no":
            break

    return user_data

result = create_dictionary()

print("Final Dictionary:")
print(result)