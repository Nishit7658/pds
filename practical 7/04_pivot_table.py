# Use pivot_table() to summarize data (e.g., average sales by Region and
# Product category).

import os
import pandas as pd

csv_path = "sales_data.csv" if os.path.exists("sales_data.csv") else os.path.join("practical 7", "sales_data.csv")

df = pd.read_csv(csv_path)
print("Sales Data Preview ::\n", df.head())

# 1. Pivot table: Average Sales by Region and Product category
pivot_avg_sales = df.pivot_table(
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="mean"
)
print("\n--- Pivot Table: Average Sales by Region and Product ---")
print(pivot_avg_sales)

# 2. Pivot table: Total Profit with Margins (subtotals/grand totals)
pivot_total_profit = df.pivot_table(
    values="Profit",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="Total"
)
print("\n--- Pivot Table: Total Profit by Region and Product (with Margins) ---")
print(pivot_total_profit)
