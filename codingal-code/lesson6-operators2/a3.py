# 1) Ask the user to enter their height in centimeters and store it in `height`.

# 2) Ask the user to enter their weight in kilograms and store it in `weight`.

# 3) Calculate BMI using the formula:
#    BMI = weight ÷ (height in meters)²
#    (Convert height from cm to meters by dividing by 100.)
#    Store the result in `BMI`.

# 4) Print the BMI value.

# 5) Use if–elif–else to decide the BMI category:
#    - If BMI is 18.4 or less → print "underweight"
#    - Else if BMI is 24.9 or less → print "healthy"
#    - Else if BMI is 29.9 or less → print "over weight"
#    - Else if BMI is 34.9 or less → print "severely over weight"
#    - Else if BMI is 39.9 or less → print "obese"
#    - Else → print "severely obese"

height=float(input("enter your height in CM: "))
weight=float(input("enter your weight in KG: "))
print("your height is ", height)
print("your weight is ", weight)
bmi=weight/(height/100)**2
print("your BMI is ", bmi)
if bmi<=18.4:
    print("You are underweight")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=29.9:
    print("You are overweight")
elif bmi<=34.9:
    print("You are severely overweight")
elif bmi<=39.9:
    print("You are obese")
else:
    print("You are severely obese")