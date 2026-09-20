# B.S. Practical 2: Revision & Open-ended Problem Solving
# Tasks:
# 1. Reads the messy CSV dataset.
# 2. Cleans the data (handles nulls, corrupted types, duplicates, and outliers).
# 3. Computes basic descriptive statistics.
# 4. Merges or groups the data to answer a specific analytical question:
#    "Which Product Category and Branch delivers the highest Net Profit Margin?"
# 5. Generates one final visualization that answers the question.

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# Step 1: Read Messy CSV Dataset
# ---------------------------------------------------------
csv_path = "messy_sales_data.csv" if os.path.exists("messy_sales_data.csv") else os.path.join("bs practical 2", "messy_sales_data.csv")
df = pd.read_csv(csv_path)

print("--- Step 1: Raw Messy Data Preview ---")
print(df.head(6))
print("\nRaw Data Shape :: ", df.shape)
print("\nMissing values in Raw Data ::\n", df.isnull().sum())

# ---------------------------------------------------------
# Step 2: Data Cleaning Pipeline
# ---------------------------------------------------------
print("\n--- Step 2: Cleaning Data ---")

# 2.1 Remove Duplicate rows
initial_rows = len(df)
df.drop_duplicates(inplace=True)
print(f"Duplicates removed :: {initial_rows - len(df)} row(s)")

# 2.2 Clean 'Sales' column (convert string "$1,200.00" to float)
if df["Sales"].dtype == "object":
    df["Sales"] = df["Sales"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False).str.strip()
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# 2.3 Handle Missing Values
# Impute numeric columns with median
df["Sales"] = df["Sales"].fillna(df["Sales"].median())
df["Discount"] = df["Discount"].fillna(df["Discount"].median())
df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].mean())

print("Missing values after imputation ::\n", df.isnull().sum())

# 2.4 Handle Outliers using IQR (Interquartile Range) on Sales
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Sales"] < lower_bound) | (df["Sales"] > upper_bound)]
print(f"\nDetected {len(outliers)} outlier(s) beyond bounds [{lower_bound:.2f}, {upper_bound:.2f}]:")
print(outliers[["Transaction_ID", "Category", "Sales", "Profit"]])

# Filter out extreme outliers
df_clean = df[(df["Sales"] >= lower_bound) & (df["Sales"] <= upper_bound)].copy()
print(f"Cleaned dataset rows :: {len(df_clean)}")

# ---------------------------------------------------------
# Step 3: Compute Basic Descriptive Statistics
# ---------------------------------------------------------
print("\n--- Step 3: Descriptive Statistics of Cleaned Dataset ---")
num_cols = ["Sales", "Profit", "Discount", "Customer_Rating"]
stats_summary = df_clean[num_cols].agg(["mean", "median", "std", "min", "max"]).T
print(stats_summary.round(2))

# ---------------------------------------------------------
# Step 4: Analytical Question:
# "Which Product Category and Branch delivers the highest Net Profit Margin?"
# ---------------------------------------------------------
print("\n--- Step 4: Grouping & Margin Analysis ---")
df_clean["Profit_Margin_%"] = (df_clean["Profit"] / df_clean["Sales"]) * 100

summary = df_clean.groupby(["Branch", "Category"]).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Avg_Margin=("Profit_Margin_%", "mean")
).reset_index()

print("Category & Branch Performance Table ::\n", summary.round(2))

top_combo = summary.sort_values(by="Avg_Margin", ascending=False).iloc[0]
print("\n========================================================")
print(f"ANALYTICAL ANSWER :: Top Performing Combination:")
print(f"Branch :: {top_combo['Branch']}")
print(f"Category :: {top_combo['Category']}")
print(f"Average Profit Margin :: {top_combo['Avg_Margin']:.2f}%")
print("========================================================")

# ---------------------------------------------------------
# Step 5: Final Visualization Answering the Question
# ---------------------------------------------------------
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

pivot_margin = df_clean.pivot_table(
    values="Profit_Margin_%",
    index="Branch",
    columns="Category",
    aggfunc="mean"
)

sns.heatmap(
    pivot_margin,
    annot=True,
    fmt=".1f",
    cmap="YlGnBu",
    linewidths=1,
    cbar_kws={"label": "Average Profit Margin (%)"}
)

plt.title("Net Profit Margin (%) by Branch and Product Category", fontsize=14, fontweight="bold")
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Store Branch", fontsize=12)
plt.tight_layout()

print("\nDisplaying Final Conclusive Visualization...")
plt.show()
