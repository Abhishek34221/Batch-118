# review = [
#     {
#     "negative":"This is very bad product i ordered one month ago",

#     "positive":"This product is very nice go  to for it ",

#     "bad_products":["Shoes","Cricket bat"],

#     "good_products":["Books","Mobile phone"]
#     }
# ]


# with open("review.txt", "w") as file:
#     for data in review:
#         file.write("Positive Review:\n")
#         file.write(data["positive"] + "\n\n")

#         file.write("Good Products:\n")
#         for product in data["good_products"]:
#             file.write(f"- {product}\n")

# print("Data saved successfully")



   
import mysql.connector

review = [
    {
        "negative": "This is very bad product i ordered one month ago",
        "positive": "This product is very nice go for it",
        "bad_products": "Shoes, Cricket bat",
        "good_products": "Books, Mobile phone"
    }
]

conn = mysql.connector.connect(host="localhost",user="root",password="abhi@123")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS product_reviews")
cursor.execute("USE product_reviews")

cursor.execute("""
CREATE TABLE IF NOT EXISTS product_review(
    negative VARCHAR(255),
    positive VARCHAR(255),
    bad_products VARCHAR(255),
    good_products VARCHAR(255)
)
""")

print("Table Created")

sql = """
INSERT INTO product_review
(negative, positive, bad_products, good_products)
VALUES (%s, %s, %s, %s)
"""

for data in review:
    values = (
        data["negative"],
        data["positive"],
        data["bad_products"],
        data["good_products"]
    )

    cursor.execute(sql, values)

conn.commit()

print("Data Inserted Successfully")

cursor.execute("SELECT * FROM product_review")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()