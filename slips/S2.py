# Create class Vehicle having attributes type, model. The class Car is vehicle having
# attributes cname, cost. The class Truck is a vehicle having attributes tname,
# cost. Display all information about light and heavy vehicle. 



class Vehicle:
    def __init__(self, vehicle_type, model):
        self.vehicle_type = vehicle_type
        self.model = model

    def display_info(self):
        """Display basic information about the vehicle."""
        print(f"Type: {self.vehicle_type}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, cname, cost, model):
        super().__init__('Car', model)
        self.cname = cname
        self.cost = cost

    def display_info(self):
        """Display information specific to the car."""
        super().display_info()
        print(f"Car Name: {self.cname}, Cost: ${self.cost:.2f}")


class Truck(Vehicle):
    def __init__(self, tname, cost, model):
        super().__init__('Truck', model)
        self.tname = tname
        self.cost = cost

    def display_info(self):
        """Display information specific to the truck."""
        super().display_info()
        print(f"Truck Name: {self.tname}, Cost: ${self.cost:.2f}")


# Example usage
if __name__ == "__main__":
    # Create instances of Car and Truck
    car1 = Car(cname="Honda Civic", cost=22000, model="2023")
    truck1 = Truck(tname="Ford F-150", cost=30000, model="2023")

    # Display information about the light vehicle (Car)
    print("Light Vehicle Information:")
    car1.display_info()
    print()  # Blank line for spacing

    # Display information about the heavy vehicle (Truck)
    print("Heavy Vehicle Information:")
    truck1.display_info()