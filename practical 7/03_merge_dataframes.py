# Use the merge() or join() function to combine two DataFrames (e.g., an
# Employee details DataFrame and a Salary details DataFrame based on
# Employee ID).

import pandas as pd

# DataFrame 1: Employee basic details
df_employee = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Nick", "Rock", "Nicky", "Rockety", "Alice"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"]
})

# DataFrame 2: Employee salary and experience details
df_salary = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 106],
    "Salary": [75000, 52000, 68000, 92000, 48000],
    "Experience_Years": [3, 2, 4, 6, 1]
})

print("Employee Details DataFrame ::\n", df_employee)
print("\nSalary Details DataFrame ::\n", df_salary)

# 1. Inner Merge (combines matching Employee_IDs)
df_inner = pd.merge(df_employee, df_salary, on="Employee_ID", how="inner")
print("\n--- Inner Merge (common Employee_IDs) ---")
print(df_inner)

# 2. Left Merge (keeps all employees from df_employee)
df_left = pd.merge(df_employee, df_salary, on="Employee_ID", how="left")
print("\n--- Left Merge (all employees from left DataFrame) ---")
print(df_left)

# 3. Outer Merge (keeps all records from both DataFrames)
df_outer = pd.merge(df_employee, df_salary, on="Employee_ID", how="outer")
print("\n--- Outer Merge (all records from both DataFrames) ---")
print(df_outer)
