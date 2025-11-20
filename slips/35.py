#  Write a recursive function to calculate the sum of numbers from 0 to n. 

def rec_fun(n):
    if n < 0:
        print("enter pos num")
    else:
        return n + rec_fun(n - 1)