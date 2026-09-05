fruits=['apple', 'banana', 'strawberry']
try:
    num=int(input("Please enter a number: "))
    if num>len(fruits):
        raise ValueError 
    else:
        print(fruits[num])
except ValueError as ve:
    print("Invalid input")
except:
    print("Error")