import csv

class Vehicle:
    def __init__(self, name, color):
        self.__name = name  
        self.color = color
        self.__engine_running__ = False

    def start_engine(self):
        if self.__engine_running__:
            print('Engine already running!')
        else:
            self.__engine_running__ = True
            print('Starting engine.')
 
    def display_info(self):
        print(f"Name: {self.__name}, Color: {self.color}")

    def return_info(self):
        return (f"Name: {self.__name}, Color: {self.color}")


class Car(Vehicle):
    def __init__(self, name, color, brand):
        super().__init__(name, color)
        self.brand = brand

    def start_engine(self):
        print("Starting the car's engine")
    
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

    def set_capacity(self, capacity):
        if capacity > 3000:
            print('This capacity is too much.')
        else:
            self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Capacity: {self.capacity}")



def save(info):
    with open("output.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        for object in info:
            data = object.return_info()
            writer.writerow(data)
        print("CSV file saved successfully!")

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
    vehicle.start_engine()

car = vehicles[0]
truck = vehicles[2]

truck.set_capacity(4000)
truck.set_capacity(2500)
truck.display_info()

save(vehicles)

print()
car.start_engine()
