# Write a NumPy program to get the unique elements of an array. 

import numpy as np

# Create a NumPy array with some duplicate elements
array = np.array([1, 2, 2, 3, 4, 4, 5, 5, 5, 6])

# Get the unique elements of the array
unique_elements = np.unique(array)

# Print the unique elements
print("Original array:", array)
print("Unique elements:", unique_elements)