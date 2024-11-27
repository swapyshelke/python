# Write a lambda expression to replace characters of given string by other character.


# Define the string and the characters to replace
original_string = "hello world"
char_to_replace = 'o'
replacement_char = '0'  # Replace 'o' with '0'

# Create a lambda function to replace characters
replace_char = lambda s, old, new: s.replace(old, new)

# Use the lambda function to replace characters in the original string
new_string = replace_char(original_string, char_to_replace, replacement_char)

# Print the result
print("Original String:", original_string)
print("Modified String:", new_string)