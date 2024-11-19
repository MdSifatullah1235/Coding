import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,600)

diamond = turtle.Turtle()
diamond.left(45)
for i in range(2):
        diamond.forward(100)  
        diamond.right(90)    
        diamond.forward(100)  
        diamond.right(90)  

turtle.done()