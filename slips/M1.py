# Write a python program to check if a string is a Palindrome or Not. 

def is_palindrome(s):
    """Check if the given string is a palindrome."""
    # Normalize the string: convert to lowercase and remove spaces
    normalized_str = s.lower().replace(" ", "")
    
    # Check if the string is equal to its reverse
    return normalized_str == normalized_str[::-1]

# Example usage
# if __name__ == "__main__":
test_string = input("Enter a string: ")
    
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')