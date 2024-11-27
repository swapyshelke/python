# Create a function showEmployee(), pass employee name and salary as parameters
# and display both, and if the salary is missing in function call it should show that
# it is Rs. 90000.


def showEmployee(name, salary=90000):
    print(f"Employee Name: {name}")
    print(f"Salary: Rs. {salary}")

# Example usage
if __name__ == "__main__":
    # Calling the function with both parameters
    showEmployee("Alice", 75000)
    
    # Calling the function with only the name parameter
    showEmployee("Bob")