# Function to find the maximum of three numbers
def find_max_of_three(num1, num2, num3):
    # Assume num1 is the maximum initially
    max_num = num1
    
    # Compare with num2
    if num2 > max_num:
        max_num = num2
    
    # Compare with num3
    if num3 > max_num:
        max_num = num3
    
    return max_num

# Input from user

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Find and print the maximum number
max_number = find_max_of_three(number1, number2, number3)
print(f"The maximum of the three numbers is: {max_number}")
