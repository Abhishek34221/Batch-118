import json
import mysql.connector

try:
   
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abhi@123"
    )

    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS product_db")
    print("✅ Database created successfully.")

   
    cursor.execute("USE product_db")

   
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        category VARCHAR(100),
        price DECIMAL(10,2),
        discountPercentage DECIMAL(5,2),
        rating DECIMAL(3,2),
        stock INT
    )
    """)
    print("✅ Table created successfully.")

    with open("product.json", "r") as file:
        product = json.load(file)

   
    sql = """
    INSERT INTO products
    (id, title, description, category, price, discountPercentage, rating, stock)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        product["id"],
        product["title"],
        product["description"],
        product["category"],
        product["price"],
        product["discountPercentage"],
        product["rating"],
        product["stock"]
    )

    cursor.execute(sql, values)
    conn.commit()

    print("✅ Product inserted successfully.")

    
    cursor.execute("SELECT * FROM products")

    print("\nProducts:")
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection Closed.")