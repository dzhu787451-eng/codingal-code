num=int(input("Please enter a number: "))
power=int(input("Please enter what number it will be to the power of: "))
x=1
for i in range(power):
    x*=num
    print(x)