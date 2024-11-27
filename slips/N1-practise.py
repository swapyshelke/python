# 123 => 123


def sum_of_digits(n):
    digit_str = str(n)
    
    total = 0
    
    for digit in digit_str:
        total += int(digit)
    
    return total


n = int(input("Enter number : "))

res = sum_of_digits(n)

print(f"Sum of digits is {res}")