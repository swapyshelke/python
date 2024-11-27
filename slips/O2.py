# Write an anonymous function to calculate area of square

# Define an anonymous function to calculate the area of a square
area_of_square = lambda side_length: side_length ** 2

# Input from the user for the side length of the square
side_length = float(input("Enter the side length of the square: "))

# Calculate the area using the anonymous function
area = area_of_square(side_length)

# Display the result
print(f"The area of the square with side length {side_length} is: {area}")