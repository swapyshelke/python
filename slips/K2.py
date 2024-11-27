# Write a NumPy program to get the unique elements of an array. 


import numpy as np

def get_unique_elements(arr):
    """Return the unique elements of a NumPy array."""
    unique_elements = np.unique(arr)
    return unique_elements

# Example usage
if __name__ == "__main__":
    # Create a NumPy array with duplicate elements
    array = np.array([1, 2, 3, 4, 2, 3, 5, 1, 6, 4, 7])
    
    # Get unique elements
    unique_array = get_unique_elements(array)
    
    # Display the result
    print("Original Array:", array)
    print("Unique Elements:", unique_array)