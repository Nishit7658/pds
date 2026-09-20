# Generate two random 3x3 matrices. Perform matrix multiplication, find the
# transpose, and calculate the determinant of the result.

import numpy as np

# Generate two random 3x3 matrices with integers between 1 and 10
matrix_a = np.random.randint(1, 10, size=(3, 3))
matrix_b = np.random.randint(1, 10, size=(3, 3))

print("Matrix A ::\n", matrix_a)
print("\nMatrix B ::\n", matrix_b)

# Matrix multiplication
result_mult = np.matmul(matrix_a, matrix_b)
print("\nMatrix Multiplication Result (A x B) ::\n", result_mult)

# Transpose of the result
result_transpose = result_mult.T
print("\nTranspose of Result ::\n", result_transpose)

# Determinant of the result
result_det = np.linalg.det(result_mult)
print("\nDeterminant of Result :: ", round(result_det, 4))
