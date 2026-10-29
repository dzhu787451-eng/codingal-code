ages=[19, 21, 25, 9, 14]
for age in ages:
    if age<18:
        print("Age not allowed", age, exit)
        exit()
    else:
        print("Age is allowed", age)
    