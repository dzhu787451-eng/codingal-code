# 1) Ask the user to enter the number of electricity units consumed and store it in `units`.

# 2) Use if–elif–else to decide the cost based on `units`:
#    - If `units` is less than 50:
#      Set `amount` as units × 2.60 and set `surcharge` as 25.
#    - Else if `units` is 100 or less:
#      Set `amount` as (cost for first 50 units) + (remaining units × 3.25)
#      Set `surcharge` as 35.
#    - Else if `units` is 200 or less:
#      Set `amount` as (cost for first 50 units) + (cost for next 50 units) + (remaining units × 5.26)
#      Set `surcharge` as 45.
#    - Else (units more than 200):
#      Set `amount` as (cost for first 50) + (next 50) + (next 100) + (remaining units × 8.45)
#      Set `surcharge` as 75.

# 3) Calculate the final bill:
#    total = amount + surcharge

# 4) Print the electricity bill (`total`) in 2 decimal places.

units=int(input("enter the number of electricty units consumed: "))
amount=0
surcharge=0
if units<=50:
    amount=units*2.60
    surcharge=25
elif units<=100:
    amount=(units*2.60)+((100-units)*3.25)
    surcharge=35
elif units<=200:
    amount=(units*2.60)+((100-units)*3.25)+((200-units)*5.26)
    surcharge=45
else:
    amount=(units*2.60)+((100-units)*3.25)+((200-units)*5.26)+((units-200)*8.45)
    surcharge=75

print("Your final electricty bill is ", amount + surcharge)