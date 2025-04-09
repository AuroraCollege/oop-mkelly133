class Vehicle:
    def __init__(self, fuel):
        self.fuel = fuel

class Motorbike(Vehicle):
    pass

class Car(Vehicle):
    pass

ninja = Motorbike('petrol')
print(ninja.fuel)

