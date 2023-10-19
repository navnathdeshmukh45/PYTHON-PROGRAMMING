#draw the Japanese flag using Python's Turtle module
from turtle import *

speed(0)
setup(800, 500)

# Move to start position
penup()
goto(0, -100)
pendown()

color("red")
begin_fill()
circle(120)
end_fill()

hideturtle()