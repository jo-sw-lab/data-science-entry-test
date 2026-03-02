from datetime import datetime


class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def describe_car(self):
        print(f"Year:{self.year} Make:{self.make} Model:{self.model}")

    def __init__(self, make, model, year):
        #Defensive coding to ensure year is numeric
        current_year = datetime.now().year
        if not isinstance(year, int) or year > current_year:
            raise ValueError("Year must be an integer and not in the future.")
    
        self.make = make
        self.model = model
        self.year = year

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
car = Car("Toyota", "Corolla", 2020)
car.describe_car()