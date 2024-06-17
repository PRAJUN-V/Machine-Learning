# Python library which provides a multidimensional array object and a set of operations for these arrays.
import numpy as np

# Create an array using numpy
arr = np.array([1, 2, 3, 4])
# print(type(arr))
# print(arr.dtype)

# Create a 2 dimensional array using numpy
two_dimensional_array = np.array([[1, 2], [3, 4.4]])
# print(two_dimensional_array)

zero_array = np.zeros((2, 2))
# zero_array[0, 0] = 1
# zero_array[0, 1] = 2
# zero_array[1, 0] = 3
# zero_array[1, 1] = 4
# print(zero_array)
# print(zero_array.dtype)

ones_array = np.ones((2, 3), dtype=int)
# print(ones_array)
# print(ones_array.dtype)

# This creates an array with random numbers as elements
arr3 = np.empty(5)
# print(arr3)  # Prints [1. 1. 1. 1. 1.]
# arr4 = np.empty((2, 3))
# print(arr4)

arr1 = np.arange(start=1, stop=20, step=0.2, dtype=float)
# print(arr1)
