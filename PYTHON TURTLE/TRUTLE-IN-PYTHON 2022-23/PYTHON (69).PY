import turtle  as  t
#for  speed of turtle 
t.penup()
t.backward(120)
t.pendown()
t.speed(10)
t.hideturtle()
a=200
#for  first  triangle turtle
for i in range(20):
    t.fd(a)
    t.left(120)
    a == 10

#for second triangle turtle
for i in  range (30):
    t.fd(a)
    t.left(130)
    a == 15
    t.mainloop