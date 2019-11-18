# Program to draw Spider Web using Turtle

import turtle

t = turtle.Pen()
colors=['red', 'blue', 'yellow', 'green', 'cyan', 'magenta']
turtle.bgcolor('black')

for i in range(190):
    t.pencolor(colors[i%6])
    t.width(2)
    t.forward(i)
    t.right(30)
