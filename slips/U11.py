# WAP to access value using key 


def check_key(dictionary, key):
    value = dictionary.get(key)
    if value is not None:
        print(f"key is present with value {value}")
    else:
        print(f"key is not present")
    

# Example dictionary
example_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

key = input("Enter key : ")
res = check_key(example_dict, key)
# print(f"value you want is {res}")