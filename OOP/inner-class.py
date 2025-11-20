class Company:
    class Employee:
        def __init__(self, name, position):
            pass
        
        def get_details(self):
            return f"{self.name} {self.position}"
    
    def __init__(self, cname):
        self.cname = cname
        self.employee = []
        
    def add_emp(self, name, position):
        new_employee = self.Employee(name, position)
        self.employee.append(new_employee)
    
    def list_emp(self):
        return [employee.get_details() for employee in self.employee]
    
company = Company("google")

company.add_emp("Swapnil", "SDE-1")
company.add_emp("Mauli", "SDE-2")
company.add_emp("Abhi", "SDE-3")


print(company.list_emp())

