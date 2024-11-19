import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,600)

polygon = turtle.Turtle()

for i in range(6):
    polygon.forward(50)
    polygon.right(60)

turtle.done()