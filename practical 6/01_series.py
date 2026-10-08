import pandas as pd

# Series from a list
s1 = pd.Series([10, 20, 30, 40, 50])
print("Series from List:\n", s1)

# Series from a dictionary
s2 = pd.Series({"Nick": 85, "Rock": 92, "Nicky": 78})
print("\nSeries from Dictionary:\n", s2)

# Slicing
print("\nSlicing:")
print(s1[1:4])

# Basic arithmetic
print("\nAddition:")
print(s1 + 5)

print("\nMultiplication:")
print(s1 * 2)