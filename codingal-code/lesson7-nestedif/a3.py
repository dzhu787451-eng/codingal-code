# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"

# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"

# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"

choice=input("Will you take Bike or Car? ")
if choice=="Bike":
    print("Options are Scooty/Scooter")
    choice2=input("Select Scooty or Scooter: ")
    if choice2=="Scooty":
        print("You have selected scooty")
    else:
        print("You have selected scooter")
elif choice=="Car":
    print("Options are Sedan/XUV")
    choice3=input("Select Sedan or XUV: ")
    if choice3=="Sedan":
        print("You have selected Sedan")
    else:
        print("You have selected XUV")
else:
    print("Wrong Choice!")
