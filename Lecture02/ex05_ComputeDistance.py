'''
Exercise05 - Compute Distance.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''
import turtle


# Simultaneous assignment, using prompt for inputing two points
x1, y1 = eval( input("Enter x1 and y1 for the 1st point: ") )  # Take the user input as interprets code.
x2, y2 = eval( input("Enter x2 and y2 for the 2nd point: ") )  # Take the user input as interprets code.

# Compute the distance
distance = ( (x1 - x2)**2 + (y1 - y2)**2 )**0.5

# Display two points and the connecting line.
turtle.showturtle()                  # Open the window (default size is 400x400).
turtle.penup()                       # Take the pen up.
turtle.goto(x1, y1)                  # Go to (x1, y1) = (User-Input, User-Input).
turtle.pendown()                     # Put the pen down. So we can draw.
turtle.color("blue")                 # Change to "blue" color for pen.
turtle.write("1st Point", font=14)   # Write the "1st Point" text on canvas with 14 font size.
turtle.color("black")                # Change to "black" color for pen.
turtle.goto(x2, y2)                  # Go to (x2, y2) = (User-Input, User-Input).
turtle.color("blue")                 # Change to "blue" color for pen.
turtle.write("2nd Point", font=14)   # Write the "2nd Point" text on canvas with 14 font size.
turtle.penup()                       # Take the pen up.

# Move to the center point of the line
turtle.goto( (x1+x2)/2, (y1+y2)/2 )  # Go to ((x1+x2)/2, (y1+y2)/2).
turtle.color("red")                  # Change to "red" color for pen.
turtle.write(distance, font=14)      # Write the distance value as a text string on canvas with 14 font size.
turtle.color("black")                # Change to "black" color for pen.

time.sleep(5)                        # Show the canvas for 5 minutes.