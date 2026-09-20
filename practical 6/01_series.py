# Create a Pandas Series from a list and a dictionary. Perform slicing and basic
# arithmetic on the Series.

import pandas as pd

# 1. Series from a list
numbers = [10, 20, 30, 40, 50]
series_from_list = pd.Series(numbers, index=['a', 'b', 'c', 'd', 'e'])
print("Series from List ::\n", series_from_list)

# 2. Series from a dictionary
student_marks = {"Nick": 85, "Rock": 92, "Nicky": 78, "Rockety": 95}
series_from_dict = pd.Series(student_marks)
print("\nSeries from Dictionary ::\n", series_from_dict)

# 3. Slicing the Series
print("\n--- Slicing ---")
print("Slice by label ['b':'d'] ::\n", series_from_list['b':'d'])
print("Slice by position [1:3] ::\n", series_from_dict.iloc[1:3])

# 4. Basic arithmetic operations on the Series
print("\n--- Arithmetic Operations ---")
print("series_from_list + 5 ::\n", series_from_list + 5)
print("series_from_list * 2 ::\n", series_from_list * 2)

# Arithmetic between two Series
series_2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("\nSecond Series ::\n", series_2)
print("Series 1 + Series 2 ::\n", series_from_list + series_2)
