# Write a program which accepts 6 integer values and prints “DUPLICATES” if any
# of the values entered are duplicates otherwise it prints “ALL UNIQUE”.
# Example: Let 6 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be
# printed.

def check_duplicates():
    # Initialize an empty set to keep track of unique values
    unique_values = set()
    
    # Get 6 integer values from the user
    print("Please enter 6 integer values:")
    for i in range(6):
        value = int(input(f"Enter integer {i + 1}: "))  # Assume valid input
        # Check if the value is already in the set
        if value in unique_values:
            print("DUPLICATES")
            return  # Exit the function if duplicates are found
        else:
            unique_values.add(value)  # Add the value to the set

    # If no duplicates were found
    print("ALL UNIQUE")

# Call the function
check_duplicates()