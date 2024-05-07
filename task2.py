import turtle

# Function to draw a Koch curve of a given length and depth
def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(t, length/3, depth-1)
        t.left(60)
        koch_curve(t, length/3, depth-1)
        t.right(120)
        koch_curve(t, length/3, depth-1)
        t.left(60)
        koch_curve(t, length/3, depth-1)

# Function to draw a Koch snowflake
def koch_snowflake(t, length, depth):
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

# Setup the Turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Koch Snowflake")
t.speed(0)  # Set the drawing speed to the fastest

# Draw the Koch snowflake
t.penup()
t.goto(-150, 90)
t.pendown()
koch_snowflake(t, 300, 4)

# Hide the Turtle and display the result
t.hideturtle()
screen.mainloop()
