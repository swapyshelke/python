# Write a Python Program to Check if a Number is Positive, Negative or Zero.


def check_number(num):
    if num > 0:
        return "The number is Positive."
    elif num < 0:
        return "The number is Negative."
    else:
        return "The number is Zero."

number = float(input("Enter a number: "))
result = check_number(number)
print(result)
