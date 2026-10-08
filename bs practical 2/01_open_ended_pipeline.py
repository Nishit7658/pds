import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read CSV
df = pd.read_csv("messy_sales_data.csv")

# 2. Clean data
df.drop_duplicates(inplace=True)

df["Sales"] = df["Sales"].replace(r"[$,]", "", regex=True).astype(float)

df["Sales"] = df["Sales"].fillna(df["Sales"].median())
df["Discount"] = df["Discount"].fillna(df["Discount"].median())
df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].mean())

# Remove Sales outliers using IQR
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Sales"] >= Q1 - 1.5 * IQR) &
        (df["Sales"] <= Q3 + 1.5 * IQR)]

# 3. Basic statistics
print("Statistics:")
print(df[["Sales", "Profit", "Discount", "Customer_Rating"]].describe().round(2))

# 4. Find highest profit margin
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

result = df.groupby(["Branch", "Category"])["Profit_Margin"].mean().reset_index()

top = result.loc[result["Profit_Margin"].idxmax()]

print("\nHighest Profit Margin:")
print(top)

# 5. Final visualization
pivot = result.pivot(index="Branch",
                     columns="Category",
                     values="Profit_Margin")

sns.heatmap(pivot, annot=True, fmt=".1f")
plt.title("Profit Margin by Branch and Category")
plt.xlabel("Category")
plt.ylabel("Branch")
plt.show()