try:
    age=int(input("Please enter your age: "))
    if age>=18:
        print("You can vote")
    else:
        print("You cannot vote")
except ValueError as ve:
    print("Invalid input")
except:
    print("Error")