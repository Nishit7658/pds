# Mini-Project - Exploratory Data Analysis (EDA)
# 1. Download a real-world dataset (e.g., Titanic Dataset from Kaggle).
# 2. Load the data using Pandas. Identify and handle missing values appropriately.
# 3. Extract statistical insights (Mean, Median, Standard Deviation) for numerical columns.
# 4. Identify and remove duplicate rows if any. Convert categorical text data into
#    numerical formats if necessary (e.g., Gender to 0/1).

import os
import urllib.request
import pandas as pd

# Task 1: Dataset loading (download if not present)
csv_path = "titanic.csv" if os.path.exists("titanic.csv") else os.path.join("practical 10", "titanic.csv")
if not os.path.exists(csv_path):
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    print("Downloading Titanic dataset from URL :: ", url)
    urllib.request.urlretrieve(url, csv_path)

df = pd.read_csv(csv_path)
print("--- Titanic Dataset Preview ---")
print(df.head())
print("\nInitial Dataset Shape :: ", df.shape)

# Task 2: Identify and handle missing values
print("\n--- Missing Values Count per Column ---")
print(df.isnull().sum())

# Handle missing Age by filling with median
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
print(f"\nMissing Age filled with median :: {median_age:.1f}")

# Handle missing Embarked by filling with mode
mode_embarked = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(mode_embarked)
print(f"Missing Embarked filled with mode :: {mode_embarked}")

# Drop Cabin due to excessive missing values
if "Cabin" in df.columns:
    df.drop(columns=["Cabin"], inplace=True)
    print("Dropped Cabin column due to high proportion of missing values.")

print("\nMissing values after cleaning ::\n", df.isnull().sum())

# Task 3: Extract statistical insights for numerical columns
numerical_cols = ["Age", "Fare", "SibSp", "Parch"]
print("\n--- Statistical Insights for Numerical Columns ---")
for col in numerical_cols:
    mean_val = df[col].mean()
    median_val = df[col].median()
    std_val = df[col].std()
    print(f"\nColumn :: {col}")
    print(f"Mean :: {mean_val:.2f}")
    print(f"Median :: {median_val:.2f}")
    print(f"Standard Deviation :: {std_val:.2f}")

# Task 4: Identify and remove duplicate rows, and convert categorical text into numerical
duplicate_count = df.duplicated().sum()
print("\n--- Duplicate Rows Check ---")
print("Number of duplicate rows found :: ", duplicate_count)
if duplicate_count > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates removed successfully.")

print("\n--- Categorical Conversion ---")
# Convert 'Sex' to numerical (male: 0, female: 1)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
print("Mapped 'Sex' column :: male -> 0, female -> 1")

# Map 'Embarked' to numerical (C: 0, Q: 1, S: 2)
df["Embarked"] = df["Embarked"].map({"C": 0, "Q": 1, "S": 2})
print("Mapped 'Embarked' column :: C -> 0, Q -> 1, S -> 2")

print("\n--- Final Cleaned DataFrame Preview ---")
print(df[["PassengerId", "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]].head())
print("\nFinal Cleaned DataFrame Info ::")
df.info()
