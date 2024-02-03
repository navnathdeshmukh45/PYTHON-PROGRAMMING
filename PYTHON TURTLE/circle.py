#draw  the circle
from turtle import *

speed(0.8)

penup()
goto(0, -100)
bgcolor("black")
color("magenta", "cyan")
pensize(10)

pendown()
begin_fill()
circle(120)
end_fill()

hideturtle()
exitonclick()