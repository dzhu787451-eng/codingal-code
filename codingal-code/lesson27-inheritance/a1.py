# 1) Create a class named `Vehicle`.

# 2) Define the constructor method `__init__(self, name, max_speed, mileage)`:
#    a) Take inputs `name`, `max_speed`, and `mileage`.
#    b) Store them as instance variables:
#       - `self.name = name`
#       - `self.max_speed = max_speed`
#       - `self.mileage = mileage`

# 3) Create a class named `Bus` that inherits from the `Vehicle` class:
#    a) Use `class Bus(Vehicle):`
#    b) Use `pass` because no extra properties or methods are added.
#    (Bus automatically gets all features of Vehicle through inheritance.)

# 4) Create an object `School_bus` of the `Bus` class by passing:
#    a) name = "School Volvo"
#    b) max_speed = 180
#    c) mileage = 12

# 5) Print the details of `School_bus` by accessing inherited instance variables:
#    a) Print the vehicle name.
#    b) Print the max speed.
#    c) Print the mileage.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):
    pass

name="School Volvo"
max_speed=180
mileage=12
School_bus=Bus(name, max_speed, mileage)

print("This is the name of the vehicle", School_bus.name)
print("This is the max speed of the vehicle", School_bus.max_speed)
print("This is the mileage of the vehicle", School_bus.mileage)
