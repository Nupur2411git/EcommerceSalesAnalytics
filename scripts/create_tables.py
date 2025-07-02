import sqlite3
import os

# Use absolute path to avoid "unable to open database" error
db_path = "E:/EcommerceSalesAnalytics/db/ecommerce.db"

# Ensure the db folder exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connect to SQLite DB (creates file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Drop tables if they already exist (optional for re-running script)
tables = ["Payments", "OrderDetails", "Orders", "Products", "Categories", "Customers"]
for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Create Customers table
cursor.execute("""
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    country TEXT
);
""")

# Create Categories table
cursor.execute("""
CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT
);
""")

# Create Products table
cursor.execute("""
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category_id INTEGER,
    price REAL,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);
""")

# Create Orders table
cursor.execute("""
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    status TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
""")

# Create OrderDetails table
cursor.execute("""
CREATE TABLE OrderDetails (
    detail_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
""")

# Create Payments table
cursor.execute("""
CREATE TABLE Payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    amount REAL,
    payment_date TEXT,
    payment_method TEXT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);
""")

conn.commit()
conn.close()
print("✅ Tables created successfully!")
