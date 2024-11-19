import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,600)

diamond = turtle.Turtle()

for i in range(24):
    diamond.forward(50)
    diamond.right(15)

turtle.done()