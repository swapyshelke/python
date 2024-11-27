# Write a Python class that has two methods: get_String and print_String, get_String
# accept a string from the user and print_String prints the string in upper case. 


class StringManipulator:
    def __init__(self):
        self.user_string = ""

    def get_string(self):
        """Accept a string from the user."""
        self.user_string = input("Enter a string: ")

    def print_string(self):
        """Print the string in uppercase."""
        print("String in uppercase:", self.user_string.upper())


# Example usage
if __name__ == "__main__":
    string_manipulator = StringManipulator()
    string_manipulator.get_string()  # Get string input from user
    string_manipulator.print_string()  # Print the string in uppercase