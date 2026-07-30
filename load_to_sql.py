import pandas as pd
import sqlite3

# Load your cleaned data
df = pd.read_csv("cleaned_orders.csv")

# Create (or connect to) a SQLite database file
conn = sqlite3.connect("retail.db")

# Load the dataframe into a SQL table called "orders"
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Data loaded into retail.db successfully!")

# Quick test query to confirm it worked
result = pd.read_sql("SELECT * FROM orders LIMIT 5;", conn)
print(result)

conn.close()