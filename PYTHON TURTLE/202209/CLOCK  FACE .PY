import turtle 

thewindow = turtle.Screen()
thewindow.bgcolor("black")

john = turtle.Turtle()
john.shape("turtle")
john.color("white")
john.pensize(4)

for  tickMark in range(12):
 john.penup()
 john.forward(180)
 john.pendown()
 john.forward(30)
 john.pendown()
 john.forward(40)
 john.stamp()
 john.backward(250)
 john.left(360/12)
thewindow.mainloop()
