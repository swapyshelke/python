# Write a Python program to calculate the average of numbers in a given list

numbers_list = [10, 20, 30, 40, 50]

def calc_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average = total / count 
    return average

average = calc_average(numbers_list)

print(average)