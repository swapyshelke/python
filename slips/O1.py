# Write a Python program to remove an item from a tuple.
# In Python, tuples are immutable, meaning that once they are created, their elements cannot be changed, added, 
# or removed directly. However, you can create a new tuple that excludes the item you want to remove.
# Here's a Python program that demonstrates how to remove an item from a tuple by creating a new tuple without the 
# specified item.


def remove_item_from_tuple(tup, item):
    """Remove the specified item from the tuple and return a new tuple."""
    # Create a new tuple without the specified item
    return tuple(x for x in tup if x != item)

# Example usage
if __name__ == "__main__":
    # Define a tuple
    my_tuple = (10, 20, 30, 40, 50)
    
    # Display the original tuple
    print("Original tuple:", my_tuple)
    
    # Input from the user for the item to remove
    item_to_remove = int(input("Enter the item to remove from the tuple: "))
    
    # Remove the item and create a new tuple
    new_tuple = remove_item_from_tuple(my_tuple, item_to_remove)
    
    # Display the new tuple
    print("New tuple after removing the item:", new_tuple)