# Create a 1D array of 10 elements and a 2D array of shape (3,4). Perform
# basic arithmetic operations (addition, multiplication) on them.

import numpy as np

arr_1d = np.arange(1, 11)
arr_2d = np.arange(1, 13).reshape(3, 4)

print("1D Array ::\n", arr_1d)
print("2D Array (shape 3x4) ::\n", arr_2d)

# Arithmetic operations with scalar
print("\n--- Scalar Operations ---")
print("1D Array + 5 ::\n", arr_1d + 5)
print("1D Array * 2 ::\n", arr_1d * 2)
print("2D Array + 10 ::\n", arr_2d + 10)
print("2D Array * 3 ::\n", arr_2d * 3)

# Arithmetic operations between arrays
print("\n--- Array Operations ---")
arr_1d_b = np.ones(10, dtype=int) * 3
print("Second 1D Array ::\n", arr_1d_b)
print("1D Array + Second 1D Array ::\n", arr_1d + arr_1d_b)
print("1D Array * Second 1D Array ::\n", arr_1d * arr_1d_b)

arr_2d_b = np.ones((3, 4), dtype=int) * 2
print("Second 2D Array ::\n", arr_2d_b)
print("2D Array + Second 2D Array ::\n", arr_2d + arr_2d_b)
print("2D Array * Second 2D Array ::\n", arr_2d * arr_2d_b)
