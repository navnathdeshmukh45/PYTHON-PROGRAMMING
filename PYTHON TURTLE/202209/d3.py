from turtle import   *
import colorsys
bgcolor('black')
speed(0)
pensize(4)
hideturtle()
hue =0.0
for i in  range(1,37):
    rt(10)
    for i in range(1,5):
      color = colorsys.hsv_to_rgb(hue,1,1)
      pencolor(color)
      hue += 0.005
      fd(200)
      rt(90)      
done()