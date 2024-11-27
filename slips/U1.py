# Write a Python script to access the value of a key from a dictionary. 

def access_value_from_dict(dictionary, key):
    """Access the value of a specified key from the dictionary."""
    # Using the get method to safely access the value
    value = dictionary.get(key)
    if value is not None:
        print(f"The value for the key '{key}' is: {value}")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

# Example dictionary
example_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}


user_key = input("Enter a key to access its value: ")
access_value_from_dict(example_dict, user_key)