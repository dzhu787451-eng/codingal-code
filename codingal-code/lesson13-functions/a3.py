# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).

# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).

# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).

# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).

# 5) Display a menu to the user showing the available operations:
#    a) Add
#    b) Subtract
#    c) Multiply
#    d) Divide

# 6) Take the user's choice as input and store it in `choice`.

# 7) Take two integer inputs from the user:
#    a) Store the first number in `num_1`
#    b) Store the second number in `num_2`

# 8) Use conditional statements to perform the chosen operation:
#    a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.
#    b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.
#    c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.
#    d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.

# 9) If the user enters anything other than a/b/c/d, print an invalid input message.

def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2
print("Select your operation from the options below")
print("a) Add")
print("b) Subtract")
print("c) Multiply")
print("d) Divide")
while True:
    choice=input("Please enter a, b, c, d, or q to quit: ")
    if choice=='q':
        break
    num_1=int(input("Please enter your first number: "))
    num_2=int(input("Please enter your second number: "))
    if choice=="a":
        print("the result is", addition(num_1, num_2))
    elif choice=="b":
        print("the result is", subtraction(num_1, num_2))
    elif choice=="c":
        print("the result is", multiplication(num_1, num_2))
    elif choice=="d":
        print("the result is", division(num_1, num_2))
    else:
        print("Invalid input")
