import pandas as pd
import sqlite3

conn = sqlite3.connect("retail.db")

# Q1: Total sales by category
q1 = """
SELECT Category, ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;
"""
print("Q1: Total Sales by Category")
print(pd.read_sql(q1, conn), "\n")

# Q2: Top 5 sub-categories by sales
q2 = """
SELECT "Sub-Category", ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY "Sub-Category"
ORDER BY Total_Sales DESC
LIMIT 5;
"""
print("Q2: Top 5 Sub-Categories by Sales")
print(pd.read_sql(q2, conn), "\n")

# Q3: Sales by region
q3 = """
SELECT Region, ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Region
ORDER BY Total_Sales DESC;
"""
print("Q3: Sales by Region")
print(pd.read_sql(q3, conn), "\n")

# Q4: Monthly sales trend
q4 = """
SELECT strftime('%Y-%m', "Order Date") AS Month, ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Month
ORDER BY Month;
"""
print("Q4: Monthly Sales Trend")
print(pd.read_sql(q4, conn), "\n")

# Q5: Top 10 customers by total spend
q5 = """
SELECT "Customer Name", ROUND(SUM(Sales), 2) AS Total_Spend
FROM orders
GROUP BY "Customer Name"
ORDER BY Total_Spend DESC
LIMIT 10;
"""
print("Q5: Top 10 Customers by Spend")
print(pd.read_sql(q5, conn), "\n")

q6 = """
SELECT strftime('%m', "Order Date") AS Month_Num, ROUND(AVG(Sales), 2) AS Avg_Monthly_Sales
FROM orders
GROUP BY Month_Num
ORDER BY Month_Num;
"""
print("Q6: Average Sales by Calendar Month (seasonality check)")
print(pd.read_sql(q6, conn), "\n")

q7 = """
SELECT strftime('%m', "Order Date") AS Month_Num, COUNT(*) AS Order_Count
FROM orders
GROUP BY Month_Num
ORDER BY Month_Num;
"""
print("Q7: Order Count by Calendar Month")
print(pd.read_sql(q7, conn), "\n")

conn.close()
