# Given a dataset of sales (Columns: Region, Salesperson, Profit), use
# groupby() to find the total profit per Region and the average profit per
# Salesperson.

import os
import pandas as pd

# Handle path whether executed from root or inside practical 7
csv_path = "sales_data.csv" if os.path.exists("sales_data.csv") else os.path.join("practical 7", "sales_data.csv")

df = pd.read_csv(csv_path)
print("Sales Dataset Preview ::\n", df.head(8))

# 1. Total profit per Region
total_profit_region = df.groupby("Region")["Profit"].sum()
print("\n--- Total Profit per Region ---")
print(total_profit_region)

# 2. Average profit per Salesperson
avg_profit_salesperson = df.groupby("Salesperson")["Profit"].mean()
print("\n--- Average Profit per Salesperson ---")
print(avg_profit_salesperson)

# Combined summary
print("\n--- Summary Statistics (Sum and Mean) by Region ---")
print(df.groupby("Region")["Profit"].agg(["sum", "mean", "count"]))
