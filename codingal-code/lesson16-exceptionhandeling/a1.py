try:
    num=int(input("Please enter a number: "))
    print("The number entered is:", num)
except ValueError as ve:
    print("Exception occured", ve)
