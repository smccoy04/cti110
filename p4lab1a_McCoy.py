import turtle

# Set up the turtle
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)  # Forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Move the turtle to a new starting position for the triangle
t.penup()           # Lift the pen up to avoid drawing
t.goto(150, 0)      # Move turtle to a new starting position
t.pendown()         # Place the pen down to start drawing

# Draw a triangle
for _ in range(3):
    t.forward(100)  # Forward by 100 units
    t.left(120)     # Turn left by 120 degrees

# Keep the window open until it's manually closed
turtle.done()