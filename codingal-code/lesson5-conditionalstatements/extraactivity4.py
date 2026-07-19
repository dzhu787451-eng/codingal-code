user_name=input("enter your username: ")
password=input("enter your password: ")
if user_name=="admin" and password=="secret": 
    print("access granted")
else:
    print("access denied")