def square_it_out(start, end):
    squares = []
    even_squares = []
    odd_squares = []
    for num in range(start, end + 1):
        sq = num ** 2
        squares.append(sq)
        if sq % 2 == 0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)
    print("All square values:", squares)
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
square_it_out(start_range, end_range)