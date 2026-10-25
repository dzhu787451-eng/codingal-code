set_a1 = {'blue', 'green'}
set_a2 = {'blue', 'yellow'}
set_b1 = {1, 2, 3, 4, 5}
set_b2 = {1, 5, 6, 7, 8, 9}
result_a = set_a1.symmetric_difference(set_a2)
result_b = set_b1.symmetric_difference(set_b2)

print(f"Symmetric difference for colors is: {result_a}")
print(f"Symmetric difference for numbers is: {result_b}")