'''
Exercise01 - Fahrenheit degree to Celsius degree.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''

import turtle
import time

def drawingStar(penSize, starLength, fillStar):
	# Initialization.
	self_angle = turtle.heading()
	turtle.right(self_angle)
	turtle.pensize(penSize)

	turtle.pendown()
	if fillStar == True:
		''' Drawing star. '''
		turtle.begin_fill()             # The begin of fill what we draw.
		for i in range(4):
			turtle.forward(starLength)
			turtle.right(144)           # Each angle of star is 36 degree (180-36=144).
		turtle.forward(starLength)
		turtle.end_fill()               # The end of fill what we draw.
		
		# Initialization of drawing arrow.
		self_angle = turtle.heading()
		turtle.right(self_angle)
		''' Filling Pentagon which in the center of star. '''
		turtle.begin_fill()             # The begin of fill what we draw.
		turtle.forward(starLength/2.58)
		for i in range(5):
			turtle.forward(starLength/4.25)
			turtle.right(72)            # Each angle of pentagon is 108 degree (180-108=72).
		turtle.end_fill()               # The end of fill what we draw.

	else:
		''' Drawing star. '''
		turtle.pensize(penSize)
		turtle.pendown()
		for i in range(4):
			turtle.forward(starLength)
			turtle.right(144)           # Each angle of star is 36 degree (180-36=144).
			# for loop
		turtle.forward(starLength)
		# if... else....
	turtle.penup()       # Take the pen up.
	# End of drawingStar() Function




turtle.showturtle()   # Open the window (default size is 400x400)
turtle.penup()        # Take the pen up.
turtle.goto(-100, 0)  # Go to (x, y) = (-208, 250).

'''
************ Drawing star *************
*The line of size is: 6.              *
*The the line length of star is: 200. *
***************************************
'''
#drawingStar(6, 150, True)
drawingStar(4, 200, False)

time.sleep(5)        # Show the canvas for 5 minutes.