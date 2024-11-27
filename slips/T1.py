# Write a program which prints Fibonacci series up to n terms. 

# def fibonacci_series(n):
#     """Function to print Fibonacci series up to n terms."""
#     if n <= 0:
#         print("Please enter a positive integer.")
#     elif n == 1:
#         print("Fibonacci series up to 1 term: 0")
#     elif n == 2:
#         print("Fibonacci series up to 2 terms: 0, 1")
#     else:
#         fib_series = [0, 1]  # Starting values for the Fibonacci series
#         while len(fib_series) < n:
#             next_term = fib_series[-1] + fib_series[-2]
#             fib_series.append(next_term)
        
#         print(f"Fibonacci series up to {n} terms: {', '.join(map(str, fib_series))}")

# # Example usage
# if __name__ == "__main__":
#     n = int(input("Enter the number of terms for Fibonacci series: "))
#     fibonacci_series(n)

num = int(input("enter number till you want series"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
    

