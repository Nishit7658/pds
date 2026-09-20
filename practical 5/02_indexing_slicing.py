# Demonstrate NumPy indexing and slicing: Extract the 2nd row and 3rd
# column from a 4x4 matrix. Replace all even numbers in the matrix with -1.

import numpy as np

matrix = np.arange(1, 17).reshape(4, 4)
print("Original 4x4 Matrix ::\n", matrix)

# Extract 2nd row (index 1) and 3rd column (index 2)
second_row = matrix[1, :]
third_col = matrix[:, 2]

print("\n2nd Row :: ", second_row)
print("3rd Column :: ", third_col)

# Replace all even numbers in the matrix with -1
matrix[matrix % 2 == 0] = -1
print("\nMatrix after replacing all even numbers with -1 ::\n", matrix)
