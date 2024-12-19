import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(500,500)

pen=turtle.Turtle()
pen.color("aqua")
pen.width(7)

size=0
while True:
    for i in range(4):
        pen.fd(size+1)
        pen.right(90)
        size=size-5
    size=size+1