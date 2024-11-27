
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# logic


max_num = num1 
# Assume num1 is the largest initially

if num2 > max_num:
    max_num = num2  # Update max_num if num2 is larger

if num3 > max_num:
    max_num = num3  # Update max_num if num3 is larger

# Print no.
print(f"The maximum number is: {max_num}")
