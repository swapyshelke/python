# Write a Python program to sum all the items in a dictionary. [10M]
# Sample Dictionary: my_dict = {'data1':100,'data2':20,'data3':50}
# Expected Result: 170 


# Sample Dictionary
my_dict = {'data1': 100, 'data2': 20, 'data3': 50}

# Function to sum all the items in the dictionary
def sum_dict_items(dictionary):
    return sum(dictionary.values())

# Calculate the sum
total_sum = sum_dict_items(my_dict)

# Display the result
print(f"The sum of all items in the dictionary is: {total_sum}")


# ==============
