class Vehicle:
    def __init__(self, name, color):
        self.__name = name  
        self.color = color 
 
    def display_info(self):
        print(f"Name: {self.__name}, Color: {self.color}")

class Car(Vehicle):
    def __init__(self, name, color, brand):
        super().__init__(name, color)
        self.brand = brand
    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")

class Bike(Vehicle):
    def __init__(self, name, color, type):
        super().__init__(name, color)
        self.type = type

class Truck(Vehicle):
    def __init__(self, name, color, capacity):
        super().__init__(name, color)
        self.capacity = capacity
    def display_info(self):
        super().display_info()
        print(f"Capacity: {self.capacity}")

def display_vehicle_info(vehicle):
    vehicle.display_info()

vehicles = [
    Car("SUV", "Black", "Toyota"),
    Bike("Sport", "Red", "Mountain"),
    Truck("Pickup", "White", "5000 lbs")
]

print("Vehicle Info")
for vehicle in vehicles:
    print()
    vehicle.display_info()