#Write a program to find the factorial using recursive function
def factorial(num):
    """ this is a function to find the factorial of any number """
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("Please enter a number: "))
print(factorial(num))
print(factorial.__doc__)
