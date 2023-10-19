import turtle
t=turtle.Turtle()
t.speed(100)
turtle.bgcolor("blue")
for i in range(240):
    t.color('cyan')
    t.circle(i)
    t.left(5)  
turtle.done()