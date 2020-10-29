# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:19:24 2020

@author: garyn
"""

# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes:
from turtle import *
from shapes import *

# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(2)

# Draw three circles:
draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

# Write a little message:
tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Teach With Code!", None, "center", "16pt bold")
tommy.goto(0,-80)

# Try changing draw_circle to draw_square, draw_triangle, or draw_star