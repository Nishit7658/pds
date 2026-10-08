# Load a sample CSV file (e.g., train.csv or iris.csv) into a DataFrame. Display
# the first 5 and last 5 rows. Use .info(), .describe(), and .shape to understand
# the data.

import pandas as pd

df = pd.read_csv("practical 6/iris.csv")

print("First 5 Rows:\n", df.head())
print("\nLast 5 Rows:\n", df.tail())

print("\nShape:", df.shape)
print("\nInfo:")
df.info()

print("\nDescribe:")
print(df.describe().iloc[:, :4].round(2))