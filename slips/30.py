# Write a lambda expression to find square of all elements in the list.

numbers = [2, 3, 4, 5, 6]


ans = list(map(lambda num: num ** 2, numbers))

print(ans)