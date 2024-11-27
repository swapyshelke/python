# Create two classes : Person class having attributes name, age and Company class
# having attributes cname, location. The class Employee will inherited from both
# classes having attributes salary, skill. Display all information of the employee. 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Company:
    def __init__(self, cname, location):
        self.cname = cname
        self.location = location

    def display_company_info(self):
        return f"Company Name: {self.cname}, Location: {self.location}"


class Employee(Person, Company):
    def __init__(self, name, age, cname, location, salary, skill):
        Person.__init__(self, name, age)
        Company.__init__(self, cname, location)
        self.salary = salary
        self.skill = skill

    def display_employee_info(self):
        person_info = self.display_person_info()
        company_info = self.display_company_info()
        return (f"{person_info}, {company_info}, "
                f"Salary: ${self.salary}, Skill: {self.skill}")


# Example usage
if __name__ == "__main__":
    # Create an Employee object
    emp = Employee(name="John Doe", age=30, cname="Tech Solutions", location="New York", salary=80000, skill="Software Development")

    # Display all information of the employee
    print(emp.display_employee_info())