import turtle
import time

turtle.showturtle()

# Initialization.
self_angle = turtle.heading()
turtle.right(self_angle)


'''
Step by step: Drawing star by using Turtle module.
'''
turtle.pensize(4)    # Change the pen size to "4".
turtle.penup()       # Take the pen up.
turtle.goto(-100,0)  # Go to (x, y) = (-100, 0).
turtle.pendown()     # Put the pen down. So we can draw.
turtle.forward(200)  # Draw a line (150) according the direction of arrow.
turtle.right(144)    # Each angle of star is 36 degree (180-36=144).
turtle.forward(200)  # Draw a line (150) according the direction of arrow.
turtle.right(144)    # Each angle of star is 36 degree (180-36=144).
turtle.forward(200)  # Draw a line (150) according the direction of arrow.
turtle.right(144)    # Each angle of star is 36 degree (180-36=144).
turtle.forward(200)  # Draw a line (150) according the direction of arrow.
turtle.right(144)    # Each angle of star is 36 degree (180-36=144).

turtle.forward(200)  # Draw a line (150) according the direction of arrow.
time.sleep(5)        # Show the canvas for 5 minutes.


"""
'''
For loop: Drawing star by using Turtle module.
'''
starLength = 200
penSize = 4
turtle.pensize(penSize)
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
for i in range(4):
	turtle.forward(starLength)
	turtle.right(144)
turtle.forward(starLength)
time.sleep(5)
"""