#.....draw letter D with python turtle........!
import turtle
t=turtle.Turtle()
t.penup()
#draw straight line
t.goto(-30,50) #centering in the screen
t.pendown()
t.pensize(10)
t.pencolor("red")
t.right(90)
t.forward(200)
 
t.penup()
t.goto(-30,50) #centering in the screen
#draw curves
t.pendown()
t.right(-90)
t.circle(-100,180)