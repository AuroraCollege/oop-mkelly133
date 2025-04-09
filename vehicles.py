class Vehicle:
    def __init__(self, fuel, mileage):
        self.fuel = fuel
        self.mileage = mileage

    def return_info(self):
        return f'Fuel: {self.fuel}, Mileage: {self.mileage}'

class Motorbike(Vehicle):
    def __init__(self, fuel, mileage, hours):
        self.hours = hours
        super().__init__(fuel, mileage)

    def return_info(self):
        return super().return_info() + f', Hours: {self.hours}'

class Car(Vehicle):
    pass

ninja = Motorbike('petrol', 5000, 25)
carolla = Car('petrol',780000)
garage = [ninja, carolla]
for vehicle in garage:
    print(vehicle.return_info())

