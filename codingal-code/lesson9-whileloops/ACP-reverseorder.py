num=int(input("Enter a number: "))
total=0
temp=num
while temp>0:
    digit=temp%10
    print(digit)
    temp=temp//10
    if digit>0:
        total+=1
print("The total amount of digits in your number is", total )
