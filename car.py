# Create a Car class with attributes like make, model, and year. 
# Then, create several Car objects and print their details.
# Extension Task: Add methods to the Car class to update the car's mileage and fuel level. 
# Create a method to calculate the fuel efficiency.

# Create the new class 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return (self.year, self.model, self.make)

Leonard = Car('Toyota', 'Corolla', 2007)
print(Leonard.display_info())

