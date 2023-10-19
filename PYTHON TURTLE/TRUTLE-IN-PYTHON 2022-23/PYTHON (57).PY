# how to code a snowman using Python's Turtle module
from turtle import *

speed(0)
setup(800, 700)

# Blue Background
penup()
goto(0, -320)
pendown()
color("lightskyblue")
begin_fill()
circle(320)
end_fill()

# Bottom of body
penup()
goto(0, -280)
pendown()
color("white")
begin_fill()
circle(110)
end_fill()

# Middle of body
penup()
goto(0, -110)
pendown()
begin_fill()
circle(90)
end_fill()

# Head of Snowman
penup()
goto(0, 20)
pendown()
begin_fill()
circle(70)
end_fill()

# Function to draw 1 small black circle
def black_circle():
    color("black")
    begin_fill()
    circle(10)
    end_fill()

# Eyes
x = -20
for i in range(2):
    penup()
    goto(x, 110)
    pendown()
    black_circle()
    x = x + 40

# Buttons
y = 0
for i in range(5):
    penup()
    goto(0, y)
    pendown()
    black_circle()
    y = y - 55

# Mouth
penup()
goto(0,70)
pendown()
color("red")
begin_fill()
circle(17)
end_fill()

penup()
goto(0,75)
pendown()
color("white")
begin_fill()
circle(17)
end_fill()
