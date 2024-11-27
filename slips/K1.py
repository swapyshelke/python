# Write a Python function that takes a number as a parameter and display factorial
# of it. 


def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage
if __name__ == "__main__":
    number = 5  # You can change this to test with other numbers
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")