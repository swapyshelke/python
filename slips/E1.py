# Write a Python program to print list after removing ODD numbers. 


def remove_odd_numbers(input_list):
    # Use list comprehension to filter out odd numbers
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

# Example input list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function and print the result
result = remove_odd_numbers(numbers)
print("List after removing ODD numbers:", result)