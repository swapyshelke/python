#  Write a program which finds sum of digits of a number.
# Example n=130 then output is 4 (1+3+0). 


def sum_of_digits(n):
    """Calculate the sum of the digits of the number n."""
    # Convert the number to a string to iterate over each digit
    digit_str = str(n)
    
    # Initialize the sum
    total = 0
    
    # Iterate over each character in the string, convert to int, and sum
    for digit in digit_str:
        total += int(digit)
    
    return total


# Input from the user
n = int(input("Enter a number: "))
    
# Calculate the sum of digits
result = sum_of_digits(n)
    
# Display the result
print(f"The sum of the digits of {n} is: {result}")