# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10. 


import numpy as np

def create_matrix():
    """Create a 3x3 matrix with values ranging from 2 to 10."""
    # Generate values from 2 to 10 (exclusive) and reshape to 3x3 matrix
    values = np.arange(2, 11)  # This generates values from 2 to 10
    matrix = values.reshape(3, 3)  # Reshape to 3x3 matrix
    return matrix

# Example usage
if __name__ == "__main__":
    matrix = create_matrix()
    print("3x3 Matrix with values ranging from 2 to 10:")
    print(matrix)