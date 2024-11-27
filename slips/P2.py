# Write a Python function to multiply all the numbers in a list.
# Sample-List: (8, 2, 3, 1, 7) Expected Output : -336


# To multiply all the numbers in a list, you can create a
# Python function that iterates through the list and 
# multiplies each number together. Below is an example of how to implement 
# this:


def multiply_numbers(numbers):
    # Initialize the result to 1 (the multiplicative identity)
    result = 1
    # Iterate through the list and multiply each number
    for number in numbers:
        result *= number
    return result

# Sample List
sample_list = (8, 2, 3, 1, 7)
# Calculate the product
product = multiply_numbers(sample_list)

# Display the result
print("Expected Output:", product)