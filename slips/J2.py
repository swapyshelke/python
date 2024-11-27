# Write a Python program to remove duplicate elements from the list. 


def remove_duplicates(input_list):
    """Remove duplicate elements from the list."""
    # Use a set to remove duplicates and convert back to list
    return list(set(input_list))

# Example usage
if __name__ == "__main__":
    # Sample list with duplicate elements
    original_list = [1, 2, 3, 4, 2, 3, 5, 1, 6]
    
    # Remove duplicates
    unique_list = remove_duplicates(original_list)
    
    # Display the result
    print("Original List:", original_list)
    print("List after removing duplicates:", unique_list)