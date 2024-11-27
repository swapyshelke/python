# Create two classes : Person class having attributes name, age and Company class
# having attributes cname , location. The class Employee will inherited from both
# classes having attributes salary, skill. Display all information of the employee. 


class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    
class Company:
    def __init__(self, cname, location):
        self.cname = cname
        self.location = location 
        
        
class Employee(Person, Company):
    def __init__(self, name, age, cname,location, salary, skill):
        Person.__init__(self, name, age)
        Company.__init__(self, cname, location)
        self.salary = salary 
        self.skill = skill
    
    def display_info(self):
        print(f"Name : {self.name}, age : {self.age}, salary : {self.salary}, skills : {self.skill}, location : {self.location}")
        

emp_1 = Employee("swapnil", 23, 20000000, "coding" , "google", "usa" )

data = emp_1.display_info()
print(data)