#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(num):
    return num*num*num
def by_3(num2):
    if num2%3==0:
        return cube(num2)
    else:
        return False
num=int(input("Please enter a number: "))
print(by_3(num))
