# Write a NumPy program to test whether every element of an 1-D array is
# present in another array. 


import numpy as np

# Create two 1-D arrays
array1 = np.array([ 1, 2, 3, 4])
array2 = np.array([])

# Check if every element of array1 is present in array2
is_present = np.isin(array1, array2)

# Check if all elements are present
all_present = np.all(is_present)

# Output the result
print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
print(f"Is every element of Array 1 present in Array 2? {all_present}")