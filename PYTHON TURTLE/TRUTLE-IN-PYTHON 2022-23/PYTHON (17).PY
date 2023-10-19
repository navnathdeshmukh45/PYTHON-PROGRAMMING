 #draw a colourful hexagonal spirograph using the Turtle module in  PYTHON #
from turtle import *

speed(0)
bgcolor("black")

colours = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(360):
    pencolor(colours[i%6])
    width(i / 250 + 1)
    forward(i)
    left(59)
    
hideturtle()