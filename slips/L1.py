# Write a Python program to count the number of occurrences of each
# character in a string. Sample String: google.com'
# Expected Result: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 


def count_characters(input_string):
    """Count the occurrences of each character in the input string."""
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count

# Example usage
if __name__ == "__main__":
    sample_string = "google.com"
    result = count_characters(sample_string)
    
    print("Sample String:", sample_string)
    print("Character Count:", result)