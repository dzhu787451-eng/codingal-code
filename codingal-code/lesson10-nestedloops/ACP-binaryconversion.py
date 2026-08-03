num=int(input("Enter a decimal number: "))
temp=num
binary=""
if temp==0:
    binary="0"
else:
    while temp>0:
        remainder=temp%2
        binary=str(remainder)+binary
        temp=temp//2
print("Your number in binary is:", binary)
