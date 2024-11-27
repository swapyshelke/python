# Write an anonymous function to display the cube of all elements in the list.

numbers = [2, 3, 4]

no = lambda x : x ** 3

cubes = list(map(no, numbers))

print(cubes)