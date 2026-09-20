# Load a sample CSV file (e.g., train.csv or iris.csv) into a DataFrame. Display
# the first 5 and last 5 rows. Use .info(), .describe(), and .shape to understand
# the data.

import os
import pandas as pd

# Handle path whether script is executed from project root or inside practical 6
csv_path = "iris.csv" if os.path.exists("iris.csv") else os.path.join("practical 6", "iris.csv")

df = pd.read_csv(csv_path)

print("--- First 5 Rows (.head()) ---")
print(df.head())

print("\n--- Last 5 Rows (.tail()) ---")
print(df.tail())

print("\n--- Shape of Dataset (.shape) ---")
print("Shape :: ", df.shape)

print("\n--- Dataset Information (.info()) ---")
df.info()

print("\n--- Statistical Summary (.describe()) ---")
print(df.describe())
