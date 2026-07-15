# 1) Create variables to store different types of values:
#    - `name` as text (string)
#    - `age` as a whole number (integer)
#    - `is_student` as True/False (boolean)
#    - `weight` as a decimal number (float)
# 2) Print each variable’s value.
# 3) Print the datatype of each variable using `type()`.
# 4) Show a message that type casting will happen next.
# 5) Convert `age` from an integer to a string and store it back in `age`.
# 6) Print `age` and print its datatype again to confirm it changed.
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
# 8) Print `weight` and print its datatype again to confirm it changed.
name="Derek"
age=14
is_student=True
weight=43.6
print("My name is", name)
print("I am", age, "years old")
print("Is Derek a student?", is_student)
print("I weigh", weight, "Kilograms")
print(type(name))
print(type(age))
print(type(is_student))
print(type(weight))
print("below will be the type casted variables")
print("the converted age is", str(age))
age=str(age)
print(type(age))
print("the converted weight is", int(weight))
weight=int(weight)
print(type(weight))