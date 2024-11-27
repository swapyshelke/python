# Create class Vehicle having attributes type, model. The class Car is vehicle having
# attributes cname, cost. The class Truck is a vehicle having attributes tname, cost.
# Display all information about light and heavy vehicle. 

class Vehicle:
    def __init__(self, vtype, model):
        self.vtype = vtype  # Vehicle type (e.g., "Car", "Truck")
        self.model = model  # Vehicle model

    def display_info(self):
        return f"Type: {self.vtype}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, cname, cost, model):
        super().__init__("Car", model)  # Call the parent constructor
        self.cname = cname  # Car name
        self.cost = cost    # Car cost

    def display_info(self):
        parent_info = super().display_info()  # Get info from Vehicle
        return f"{parent_info}, Car Name: {self.cname}, Cost: {self.cost}"


class Truck(Vehicle):
    def __init__(self, tname, cost, model):
        super().__init__("Truck", model)  # Call the parent constructor
        self.tname = tname  # Truck name
        self.cost = cost     # Truck cost

    def display_info(self):
        parent_info = super().display_info()  # Get info from Vehicle
        return f"{parent_info}, Truck Name: {self.tname}, Cost: {self.cost}"


# Example usage
# if __name__ == "__main__":

# Creating instances of Car and Truck
car1 = Car(cname="Toyota Corolla", cost=20000, model="2023")
truck1 = Truck(tname="Ford F-150", cost=30000, model="2024")

# Displaying information about the vehicles
print("Light Vehicle Information:")
print(car1.display_info())
    
print("\nHeavy Vehicle Information:")
print(truck1.display_info())