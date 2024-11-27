# Create a function showEmployee(), pass employee name and salary as parameters
# and display both, and if the salary is missing in function call it should show that
# it is Rs. 90000.

def showEmployee(name, salary = 90000):
    print(f"Name : {name}")
    print(f"salary : {salary}")
    
    
print(showEmployee("Swapnil", 1000))