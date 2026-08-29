import math
def calcirc(radius):
    circumference=2*math.pi*radius
    return circumference
radius=int(input("Please enter your intended radius for your circle: "))
result=calcirc(radius)
print("The circumference is around", round(result,2))
