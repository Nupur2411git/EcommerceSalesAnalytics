import sqlite3

# Connect to the DB
conn = sqlite3.connect("E:/EcommerceSalesAnalytics/db/ecommerce.db")
cursor = conn.cursor()

# View some rows from each table
tables = ["Customers", "Categories", "Products", "Orders", "OrderDetails", "Payments"]

for table in tables:
    print(f"\n📦 {table} Data:")
    cursor.execute(f"SELECT * FROM {table} LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()
