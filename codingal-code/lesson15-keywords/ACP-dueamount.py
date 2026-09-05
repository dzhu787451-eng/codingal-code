def calc(total_cost, amount_paid):
    cost=amount_paid-total_cost
    return cost
bill=float(input("Enter the cost of the bill: "))
paid=float(input("Enter how much you have paid: "))
change=calc(bill, paid)
print("The shop keeper should give back:", round(change, 2))