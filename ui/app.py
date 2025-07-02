import streamlit as st
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("E:/EcommerceSalesAnalytics/db/ecommerce.db")

st.set_page_config(page_title="📊 E-Commerce Sales Dashboard", layout="wide")

st.title("🛒 E-Commerce Sales Analytics Dashboard")

# Load data
df_customers = pd.read_sql_query("SELECT * FROM Customers", conn)
df_orders = pd.read_sql_query("SELECT * FROM Orders", conn)
df_order_details = pd.read_sql_query("SELECT * FROM OrderDetails", conn)
df_products = pd.read_sql_query("SELECT * FROM Products", conn)
df_payments = pd.read_sql_query("SELECT * FROM Payments", conn)

# Merge for analytics
merged = df_orders.merge(df_order_details, on="order_id") \
                  .merge(df_products, on="product_id") \
                  .merge(df_customers, on="customer_id") \
                  .merge(df_payments, on="order_id")

# Show KPIs
st.subheader("📈 Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{int(merged['amount'].sum())}")
col2.metric("Total Orders", df_orders.shape[0])
col3.metric("Total Customers", df_customers.shape[0])

st.markdown("---")

# Sales by Category
st.subheader("📦 Sales by Product Category")
sales_by_cat = merged.groupby("category_id")["amount"].sum().reset_index()
df_categories = pd.read_sql_query("SELECT * FROM Categories", conn)
sales_by_cat = sales_by_cat.merge(df_categories[["category_id", "category_name"]], on="category_id", how="left")

st.bar_chart(sales_by_cat.set_index("category_name")["amount"])

# Orders over Time
st.subheader("🕒 Orders Over Time")
orders_time = df_orders.groupby("order_date").size().reset_index(name="Order Count")
st.line_chart(orders_time.set_index("order_date"))

# Customer Table
st.subheader("👥 Customers")
st.dataframe(df_customers)

conn.close()
