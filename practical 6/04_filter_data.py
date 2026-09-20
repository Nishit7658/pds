# Select specific columns and filter rows where the Salary/Age is greater than a
# certain threshold using .loc and .iloc.

import pandas as pd

employee_data = {
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Nick", "Rock", "Nicky", "Rockety", "Alice", "Bob"],
    "Age": [22, 28, 24, 32, 29, 21],
    "Dept": ["IT", "HR", "Finance", "IT", "Marketing", "Finance"],
    "Salary": [75000, 52000, 68000, 92000, 58000, 48000]
}

df = pd.DataFrame(employee_data)
print("Original DataFrame ::\n", df)

# Filter using .loc (label/condition based)
# Filtering employees where Salary > 60000 and selecting Name, Dept, Salary
salary_threshold = 60000
print(f"\n--- Filtering with .loc (Salary > {salary_threshold}) ---")
filtered_loc = df.loc[df["Salary"] > salary_threshold, ["Name", "Dept", "Salary"]]
print(filtered_loc)

# Filtering employees where Age > 25
age_threshold = 25
print(f"\n--- Filtering with .loc (Age > {age_threshold}) ---")
filtered_age = df.loc[df["Age"] > age_threshold, ["Name", "Age", "Dept"]]
print(filtered_age)

# Slicing and filtering using .iloc (integer-position based)
# Selecting rows 0 to 3 and columns 1 to 4 (Name, Age, Dept, Salary)
print("\n--- Selecting with .iloc (first 4 rows and columns 1 to 3) ---")
filtered_iloc = df.iloc[0:4, 1:4]
print(filtered_iloc)
