# Write a recursive function to calculate the sum of numbers from 0 to n. 


# def recursive_sum(n):
#     # Base case: if n is 0, the sum is 0
#     if n == 0:
#         return 0
#     else:
#         # Recursive case: sum of n and the sum of numbers from 0 to n-1
#         return n + recursive_sum(n - 1)

# # Input from the user

# number = int(input("Enter a non-negative integer: "))
# if number < 0:
#     print("Please enter a non-negative integer.")
# else:
#     result = recursive_sum(number)
#     print(f"The sum of numbers from 0 to {number} is: {result}")










# Write a recursive function to calculate the sum of numbers from 0 to n. 


def rec_sum(n):
    # base condition
    if n == 0:
        return
    else:
        return n + rec_sum(n - 1)

num = int(input("Enter any non-negative number : "))

if num <= 0:
    print("Enter positive number")
else:
    res = rec_sum(num)
    print(f"final result is : {res}")
    
    
