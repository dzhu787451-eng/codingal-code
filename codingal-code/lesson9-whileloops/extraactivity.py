num=str(input("Please enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    print(digit)
    sum+=digit
    temp=temp//10
print("The sum of the digits added is", sum)