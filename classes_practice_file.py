#1.create a Vehicle class with max_speed and mileage instance attributes.
'''class Vehical:

    def __init__(self, speed = None, mil = None):
        self.max_speed = speed
        self.mileage = mil

Ninja = Vehical(250, 20)
print(Ninja.mileage)'''

#2.Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
'''class Vehical:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehical):
    pass

SchoolBus = Bus("Kedar Nath", 120, 15)
print(SchoolBus.name)'''

#3.Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
'''class Vehical:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."

class Bus(Vehical):

    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

SchoolBus = Bus("School Bus", 100, 15)
print(SchoolBus.seating_capacity())'''

#4.Define a property that must have the same value for every class instance (object)
#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
'''class Vehical:

    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehical):
    pass

class Car(Vehical):
    pass

Honda = Car("Xcent", 180, 20)
SchoolBus = Bus("Bus", 120, 10)
print(Honda.color, SchoolBus.color)'''

#5.Create a Bus child class that inherits from the Vehicle class. The default fare charge of
#  any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% 
# on full fare as a maintenance charge. So total fare for bus instance will become 
# the final amount = total fare + 10% of the total fare.

'''class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return super().fare() + super().fare()/10

VolvoBus = Bus("VolvoBus", 20, 50)
print(VolvoBus.fare())
'''























