import json

with open("product.json","r") as file:
   python_data=json.load(file)
 
with open("product_details.txt", "w") as file:
    for key, value in python_data.items():
        file.write(f"{key} : {value}\n")

print("Data saved successfully ✅")