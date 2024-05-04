import turtle

# Set up the turtle
t = turtle.Turtle()

# Drawing the letter s

t.penup()
t.setpos(-100, 100)
t.pendown()
t.right(5)
t.backward(10)
t.backward(30)
t.circle(-90, -180)
t.circle(90, -180)
t.backward(50)
t.right(10)
t.backward(10)
t.right(5)
t.backward(10)
t.right(5)
t.backward(10)
t.right(10)
t.backward(5)

# Drawing the letter M

t.penup()
t.goto(-10,100)
t.pendown()
t.right(55)
t.forward(150)
t.backward(150)
t.left(45)
t.forward(90)
t.left(95)
t.forward(90)
t.right(140)
t.forward(150)