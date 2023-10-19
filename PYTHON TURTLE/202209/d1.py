import turtle 

ob = turtle.Turtle()
ob.speed(15)
d =200
angle =140
for i in range(1,300):
 ob.forward(d)
 ob.left(angle)
 d=d-1