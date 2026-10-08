# Create a 1D array of 10 elements and a 2D array of shape (3,4). Perform
# basic arithmetic operations (addition, multiplication) on them.

import numpy as np

arr_1d = np.arange(1, 11)
arr_2d = np.arange(1, 13).reshape(3, 4)

print("1D Array:")
print(arr_1d)

print("\n2D Array:")
print(arr_2d)

print("\n1D Array + 5:")
print(arr_1d + 5)

print("\n1D Array * 2:")
print(arr_1d * 2)

print("\n2D Array + 5:")
print(arr_2d + 5)

print("\n2D Array * 2:")
print(arr_2d * 2)