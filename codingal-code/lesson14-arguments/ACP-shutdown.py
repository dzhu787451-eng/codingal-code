def shutdown(user_input):
    user_input=user_input.lower()
    if user_input=="yes":
        return "Shutting Down"
    elif user_input=="no":
        return "Abandon Shut Down"
    else:
        return "Sorry"
choice=input("Would you like to shut down? (Yes or No): ")
result=shutdown(choice)
print(result)    