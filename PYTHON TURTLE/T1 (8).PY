#Q1. draw  th square   in python 
from   turtle import *
speed(0.7)
bgcolor("black")

#outlined square 
penup()
goto(-350,100)
pendown()
pensize(5)
color("magenta")

for i in range (4):
    forward(150)
    left(90)
    
#multicolored square(stroke only)
penup()
goto(-150,100)
pendown()

for i in ["yellow","red","blue","purple"]:
    color(i)
    forward(150)
    left(90)
    
#square with  fill and  stroke 
penup()
goto(0,100)
color("orange","yellow")
pendown()
begin_fill()

for i in range(4):
    forward(150)
    left(90)
    end_fill
