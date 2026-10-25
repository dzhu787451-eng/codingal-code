def calculate_tuple_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product
tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2, 9)
result1 = calculate_tuple_product(tuple1)
result2 = calculate_tuple_product(tuple2)
print(f"The product of elements in tup1 {tuple1} is: {result1}")
print(f"The product of elements in tup2 {tuple2} is: {result2}")