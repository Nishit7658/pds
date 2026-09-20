# Load the built-in tips or iris dataset from Seaborn.

import seaborn as sns

# Load built-in 'tips' dataset
tips = sns.load_dataset("tips")

print("--- Tips Dataset First 5 Rows (.head()) ---")
print(tips.head())

print("\n--- Tips Dataset Information (.info()) ---")
tips.info()

print("\n--- Tips Dataset Summary Statistics (.describe()) ---")
print(tips.describe())

# Load built-in 'iris' dataset
iris = sns.load_dataset("iris")
print("\n--- Iris Dataset First 5 Rows (.head()) ---")
print(iris.head())
print("\nIris Dataset Shape :: ", iris.shape)
