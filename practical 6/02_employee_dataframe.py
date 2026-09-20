# Create a DataFrame from a dictionary containing Employee details (ID,
# Name, Dept, Salary).

import pandas as pd

employee_data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Nick", "Rock", "Nicky", "Rockety", "Alice"],
    "Dept": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [75000, 52000, 68000, 92000, 58000]
}

df_employee = pd.DataFrame(employee_data)

print("Employee DataFrame ::\n", df_employee)
print("\nDataFrame Info ::")
df_employee.info()
print("\nDataFrame Shape :: ", df_employee.shape)
print("\nDataFrame Columns :: ", df_employee.columns.tolist())
