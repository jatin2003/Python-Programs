# Program to draw Polygon using Turtle

import turtle

polygon = turtle.Turtle() 

sides = 8                      # Change no. of sides
length = 60                    # Length of Polygon Sides
angle = 360.0 / sides       

for i in range(sides): 
	polygon.forward(length) 
	polygon.right(angle) 
	
turtle.done() 
