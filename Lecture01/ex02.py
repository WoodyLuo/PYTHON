'''
Exercise02 - Give the turtle module a try.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''

import turtle
import time

turtle.screensize(550,550)  # Set the screensize for canvas.
turtle.showturtle()         # Open the window (default size is 400x400)
turtle.bgcolor("gray")      # Set the "grat" color for the background of cancas.
turtle.penup()              # Take the pen up.
turtle.goto((-250,250))     # Go to (x, y) = (-250, 250).
turtle.write("Welcome")     # Write the "Welcome" text on canvas.
turtle.goto((-208,250))     # Go to (x, y) = (-208, 250).
turtle.color("orange")      # Change to "orange" color for pen.
# Set the font size and align.
turtle.write("to", move=True, align="left", font=("Arial", 24, "normal"))
turtle.color("black")       # Change to "black" color for pen.
# Set the font size and align.
turtle.write(" Python", move=True, align="left", font=("Arial", 42, "normal"))
turtle.goto((-150,150))     # Go to (x, y) = (-150, 150).

## Here, we did not put the pen down. So, we can not see the circle. ##
turtle.circle(50)           # Draw a circle of radius 5.


turtle.pendown()            # Put the pen down. So we can draw.
turtle.circle(50)           # Draw a circle of radius 5.
turtle.forward(150)         # Draw a line (150) according the direction of arrow.
turtle.right(90)            # Turning right 90 degrees of the arrow.
turtle.forward(50)          # Draw a line (50) according the direction of arrow.
turtle.right(-270)          # Turning right -270 degrees of the arrow.
turtle.forward(170)         # Draw a line (50) according the direction of arrow.
turtle.right(45)            # Turning right 45 degrees of the arrow.
turtle.color("red")         # Change to "red" color for pen.
turtle.pensize(18)          # Change the pen size to "18".
turtle.forward(150)         # Draw a line (150) according the direction of arrow.
turtle.penup()              # Take the pen up.
turtle.color("blue")        # Change to "blue" color for pen.
turtle.goto((-150,0))       # Go to (x, y) = (-150, 0).
turtle.pendown()            # Put the pen down. So we can draw.
turtle.pensize(4)           # Change the pen size to "4".

turtle.begin_fill()         # The begin of fill what we draw
turtle.circle(50)           # Draw a circle of radius 5.
turtle.end_fill()           # The end of fill what we draw

time.sleep(5)               # Show the canvas for 5 minutes.

