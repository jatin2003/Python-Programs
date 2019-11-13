#!/bin/python3

# Turtle Race Game

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for i in range(15):
  write(i,align = 'center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

red = Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-160, 100)
red.pendown()

for j in range(10):
  red.right(36)

blue = Turtle()
blue.color('yellow')
blue.shape('turtle')
blue.penup()
blue.goto(-160, 70)
blue.pendown()

for j in range(72):
  blue.left(5)

green = Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-160, 40)
green.pendown()

for j in range(60):
  green.right(6)

yellow = Turtle()
yellow.color('blue')
yellow.shape('turtle')
yellow.penup()
yellow.goto(-160, 10)
yellow.pendown()

for j in range(30):
  yellow.left(12)

for j in range(100):
  red.forward(randint(1,5))
  blue.forward(randint(1,5))
  green.forward(randint(1,5))
  yellow.forward(randint(1,5))
