# Write a Python program to check whether a given element is present in the given
# tuple. Display the appropriate message. 


def check_element_in_tuple(element, tup):
    """Check if the given element is present in the tuple."""
    return element in tup


# Define a tuple
my_tuple = (10, 20, 30, 40, 50)
    
# Input from the user
user_input = input("Enter an element to check in the tuple: ")
    

    # Attempt to convert to integer
element_to_check = int(user_input)
    
# Check if the element is in the tuple
if check_element_in_tuple(element_to_check, my_tuple):
    print(f"The element {element_to_check} is present in the tuple.")
else:
    print(f"The element {element_to_check} is not present in the tuple.")