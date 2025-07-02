import sqlite3

# Connect to the existing DB
conn = sqlite3.connect("E:/EcommerceSalesAnalytics/db/ecommerce.db")
cursor = conn.cursor()

# Sample Customers (India-based)
cursor.executemany("""
INSERT INTO Customers (customer_id, name, email, country)
VALUES (?, ?, ?, ?)
""", [
    (1, "Amit Sharma", "amit.sharma@example.com", "India"),
    (2, "Priya Mehta", "priya.mehta@example.com", "India"),
    (3, "Rahul Verma", "rahul.verma@example.com", "India"),
])

# Sample Categories
cursor.executemany("""
INSERT INTO Categories (category_id, category_name)
VALUES (?, ?)
""", [
    (1, "Electronics"),
    (2, "Books"),
    (3, "Apparel"),
])

# Sample Products
cursor.executemany("""
INSERT INTO Products (product_id, product_name, category_id, price)
VALUES (?, ?, ?, ?)
""", [
    (1, "Smartphone", 1, 15000),
    (2, "Bluetooth Speaker", 1, 2500),
    (3, "Self-Help Book", 2, 499),
    (4, "Kurti", 3, 899),
])

# Sample Orders
cursor.executemany("""
INSERT INTO Orders (order_id, customer_id, order_date, status)
VALUES (?, ?, ?, ?)
""", [
    (1, 1, "2025-06-10", "Delivered"),
    (2, 2, "2025-06-11", "Shipped"),
    (3, 3, "2025-06-12", "Cancelled"),
])

# Sample OrderDetails
cursor.executemany("""
INSERT INTO OrderDetails (detail_id, order_id, product_id, quantity, unit_price)
VALUES (?, ?, ?, ?, ?)
""", [
    (1, 1, 1, 1, 15000),
    (2, 1, 2, 1, 2500),
    (3, 2, 3, 2, 499),
    (4, 3, 4, 1, 899),
])

# Sample Payments
cursor.executemany("""
INSERT INTO Payments (payment_id, order_id, amount, payment_date, payment_method)
VALUES (?, ?, ?, ?, ?)
""", [
    (1, 1, 17500, "2025-06-10", "UPI"),
    (2, 2, 998, "2025-06-11", "Debit Card"),
])

conn.commit()
conn.close()
print("✅ sample data inserted successfully!")
