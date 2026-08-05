rows=int(input("Please enter the number of rows you want: "))
for i in range(1, rows+1):
    for j in range(rows-1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
