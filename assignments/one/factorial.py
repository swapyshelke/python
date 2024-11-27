print("Program to find factorial")

def factorial():
	print("Enter number till you want to use factorial")
	n = int(input())
	if n < 0:
	   print("sorry, factorial doesnt exist for negative numbers")
	elif n == 0:
	    print("the factorial of zero is one")
	else:
	    for i in range(1, num + 1):
	      factorial = factorial * i
             print(f"the factorial of {n} is {factorial}")
	

factorial()