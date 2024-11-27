# Write an anonymous function to display the cube of all elements in the list.

# Sample list of numbers
sample_list = [1, 2, 3, 4, 5]

# Using a lambda function to calculate the cube of each element
cubes = list(map(lambda x: x ** 3, sample_list))

# Display the result
print("Cubes of all elements in the list:", cubes)