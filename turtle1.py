import turtle

x = turtle.Turtle()
y = 5
z = 50
a = 360.0 / y
for i in range(y):
  x.forward(z)
  x.right(a)

turtle.done()