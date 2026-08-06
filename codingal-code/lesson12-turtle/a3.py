# 1) Import the `turtle` library to use turtle graphics.

# 2) Create a turtle screen window and store it in `my_wn`.

# 3) Set up the screen:
#    a) Change the background color to "light blue".
#    b) Set the window title to "Turtle".

# 4) Create a Turtle object and store it in `my_pen`.
#    (This turtle will draw the pattern.)

# 5) Initialize `size = 0`.
#    (This variable controls how long each side of the square will be.)

# 6) Start an infinite loop using `while True` so the drawing continues forever.

# 7) Inside the infinite loop, draw a square using a `for` loop that runs 4 times:
#    a) Move the turtle forward by `size + 1`.
#    b) Turn the turtle left by 90 degrees to make a right angle.
#    c) Decrease `size` by 5 after each side.

# 8) After completing one square (4 sides), increase `size` by 1.
#    (This changes the size value for the next iteration, creating a repeating pattern.)

import turtle
my_wn=turtle.Screen().setup(600,500)
turtle.Screen().bgcolor("light blue")
turtle.title("Turtle")
my_pen=turtle.Turtle()
size=0
x=0
temp=True
while temp==True:
    for i in range(4): 
        my_pen.forward(size+1)
        my_pen.left(90)
        size-=5
    size+=1
    x+=1
    if x==5:
        temp=False
