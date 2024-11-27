# Write a Python program to find the Factorial of a Number


# Example Code (Iterative Approach)


# def factorial_iterative(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# # Example usage
# if __name__ == "__main__":
#     number = int(input("Enter a number to find its factorial: "))
#     print(f"The factorial of {number} is: {factorial_iterative(number)}")










# Example Code (Recursive Approach)


# def factorial_recursive(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)

# # Example usage
# if __name__ == "__main__":
#     number = int(input("Enter a number to find its factorial: "))
#     print(f"The factorial of {number} is: {factorial_recursive(number)}")














# factorial using recursive approach

def fact_func(num):
    if num < 0:
        print("Enter posittive number")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * fact_func(num - 1)


number = int(input("Enter number : "))

res = fact_func(number)
print(res)
    