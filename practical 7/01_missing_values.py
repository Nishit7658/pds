# Create a DataFrame with some NaN (null) values. Practice dropping rows
# with dropna() and filling missing values with mean/median using fillna().

import numpy as np
import pandas as pd

# Creating DataFrame with missing (NaN) values
data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Nick", "Rock", np.nan, "Rockety", "Alice", "Bob", "Charlie"],
    "Score": [88.0, np.nan, 75.0, 92.0, np.nan, 64.0, 85.0],
    "Age": [20.0, 21.0, np.nan, 22.0, 20.0, np.nan, 23.0]
}

df = pd.DataFrame(data)
print("Original DataFrame with NaN ::\n", df)

# Check null values count per column
print("\nNull values count per column ::\n", df.isnull().sum())

# 1. Dropping rows with any null value
df_dropped = df.dropna()
print("\n--- After dropna() (dropping any row with NaN) ---")
print(df_dropped)

# 2. Imputing / Filling missing values
# Filling Score column with mean, and Age column with median
df_filled = df.copy()

mean_score = df["Score"].mean()
median_age = df["Age"].median()

print(f"\nCalculated Mean Score :: {mean_score:.2f}")
print(f"Calculated Median Age :: {median_age:.1f}")

df_filled["Score"] = df_filled["Score"].fillna(mean_score)
df_filled["Age"] = df_filled["Age"].fillna(median_age)
df_filled["Name"] = df_filled["Name"].fillna("Unknown")

print("\n--- After fillna() (Score with mean, Age with median) ---")
print(df_filled)
