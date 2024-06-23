# Import required modules
from abc import ABC, abstractmethod

# Create Abstract Base Class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method
    @abstractmethod
    def printDetails(self):
        pass
    
    # Create concrete method
    def accelerate(self):
        print("Speeding up...")

    def brake(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    # Implement the abstract method
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
    
    # Add a specific method for this class
    def Sunroof(self):
        print("Not having this feature")

# Create another child class
class Suv(Car):
    # Implement the abstract method
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
    
    # Add a specific method for this class
    def Sunroof(self):
        print("Available")

# Instantiate objects of the concrete classes
car1 = Hatchback("Maruti", "Alto", "2022")
car2 = Suv("Toyota", "Fortuner", "2023")

# Call methods on the objects
car1.printDetails()
car1.accelerate()
car1.brake()
car1.Sunroof()

print()  # Just to add a newline for clarity

car2.printDetails()
car2.accelerate()
car2.brake()
car2.Sunroof()
