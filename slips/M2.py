#  Create class Vehicle having attributes type, model. The class Car is vehicle having
# attributes cname, cost. The class Truck is a vehicle having attributes tname, cost.
# Display all information about light and heavy vehicle. 


class Vehicle:
    def __init__(self, vehicle_type, model):
        self.vehicle_type = vehicle_type
        self.model = model

    def display_info(self):
        return f"Type: {self.vehicle_type}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, cname, cost, vehicle_type, model):
        super().__init__(vehicle_type, model)
        self.cname = cname
        self.cost = cost

    def display_info(self):
        return f"Car Name: {self.cname}, Cost: {self.cost}, " + super().display_info()


class Truck(Vehicle):
    def __init__(self, tname, cost, vehicle_type, model):
        super().__init__(vehicle_type, model)
        self.tname = tname
        self.cost = cost

    def display_info(self):
        return f"Truck Name: {self.tname}, Cost: {self.cost}, " + super().display_info()


# Example usage
if __name__ == "__main__":
    # Creating instances of Car and Truck
    car1 = Car(cname="Toyota Camry", cost=24000, vehicle_type="Light Vehicle", model="2022")
    truck1 = Truck(tname="Ford F-150", cost=30000, vehicle_type="Heavy Vehicle", model="2022")

    # Displaying information about the vehicles
    print("Vehicle Information:")
    print(car1.display_info())
    print(truck1.display_info())