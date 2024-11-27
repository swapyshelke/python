# Write a Python Program to Find the Factorial of a Number. 

def fact(n):
    if n < 0:
        pass 
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

number = int(input("enter any number : "))

res = fact(number)
print(res)