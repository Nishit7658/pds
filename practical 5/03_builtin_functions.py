# Use NumPy built-in functions: np.zeros, np.ones, np.arange, np.linspace, and
# np.reshape.

import numpy as np

# 1. np.zeros
zeros_arr = np.zeros((3, 3))
print("np.zeros (shape 3x3) ::\n", zeros_arr)

# 2. np.ones
ones_arr = np.ones((2, 4))
print("\nnp.ones (shape 2x4) ::\n", ones_arr)

# 3. np.arange
arange_arr = np.arange(10, 50, 5)
print("\nnp.arange(10, 50, 5) ::\n", arange_arr)

# 4. np.linspace
linspace_arr = np.linspace(0, 10, 5)
print("\nnp.linspace(0, 10, 5) ::\n", linspace_arr)

# 5. np.reshape
original_arr = np.arange(12)
reshaped_arr = np.reshape(original_arr, (3, 4))
print("\nOriginal array for reshape ::\n", original_arr)
print("np.reshape into (3, 4) ::\n", reshaped_arr)
