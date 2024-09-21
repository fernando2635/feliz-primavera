from turtle import *
from math import *

speed(5000)
bgcolor("black")
goto(0,-40)

#draw leaves
for i in range(16):
    for j in range(18):
        color("#ffa216"), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6, 90), rt(180)
    circle(40,24)

#draw flower center
color("black")
shape("circle")
shapesize(0.5)
fillcolor("#884513")
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x, y)
    setheading(i*golden_ang)
    pendown(), stamp()

#define points to draw letters
def point(x, y):
    penup(), goto(x, y), pendown()
    color("black"), fillcolor("#ffa216")
    begin_fill(), circle(4), end_fill()

#function to draw "T"
def draw_T(x, y):
    positions_t=[(x, y+30), (x+6, y+30), (x+12, y+30), (x+18, y+30),
                  (x+24, y+30), (x+12, y+30), (x+12, y+24), (x+12, y+18),
                  (x+12, y+12), (x+12, y+6), (x+12, y)]
    
    for pos in positions_t:
        point(*pos)

#function to draw "Ú"
def draw_U(x, y):
    positions_u=[(x, y+30), (x, y+24), (x, y+18), (x, y+12),(x, y+6),
                  (x+3, y+3), (x+6, y), (x+12, y-1), (x+18, y),
                  (x+21, y+3), (x+24, y+6), (x+24, y+12), (x+24, y+18),
                  (x+24, y+24), (x+24, y+30), (x+12, y+36), (x+16, y+40)]
    
    for pos in positions_u:
        point(*pos)

#draw "TÚ"
draw_T(-27, -20)
draw_U(7, -20)

hideturtle()
done()
