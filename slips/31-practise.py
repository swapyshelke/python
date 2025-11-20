# Create class Vehicle having attributes type, model. The class Car is vehicle having
# attributes cname, cost. The class Truck is a vehicle having attributes tname, cost.
# Display all information about light and heavy vehicle. 

class Vehicle:
    def __init__(self, type, model):
        self.type = type
        self.model = model 
    
    def show(self):
        print(f"type : {self.type}, model : {self.model}")
        
class Car(Vehicle):
    def __init__(self, cname, cost, model):
        super().__init__("Car", model)
        self.cname = cname
        self.cost = cost 
        
    def show(self):
        parent_info = super().show()
        print(f"Car name : {self.cname}, cost : {self.cost}")
        

car1 = Car("car name", 1000, "type")
print(car1.cname)
print(car1.cost)
print(car1.model)
car1.show()
        