'''
Laboratory01 - Compute Triangle Area.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''

# x1, y1, x2, y2, x3, y3 = 1.5, -3.4, 4.6, 5, 9.5, -3.4

# Simultaneous assignment three point, using prompt for inputing two points
x1, y1, x2, y2, x3, y3  = eval( input("Enter x1, y1, x2, y2, x3, y3 for the 1st point: ") )  # Take the user input as interprets code.

# Side1 is a length of triangle that is point1 (x1, y1) connect to point2 (x2, y2).
side1 = ( (x1 - x2)**2 + (y1 - y2)**2 )**0.5  # Compute distance of side lenght 1 of triangle

# Side2 is a length of triangle that is point1 (x2, y2) connect to point2 (x3, y3).
side2 = ( (x2 - x3)**2 + (y2 - y3)**2 )**0.5  # Compute distance of side lenght 2 of triangle

# Side3 is a length of triangle that is point1 (x3, y3) connect to point2 (x1, y1).
side3 = ( (x3 - x1)**2 + (y3 - y1)**2 )**0.5  # Compute distance of side lenght 3 of triangle

# Compute the semi perimeter(半週長).
s = ( side1+side2+side3 ) * 0.5
print("Semi perimeter of triangle is:", s)  # Print the semi perimeter out.

# Computer the area of triangle.
triangleArea = ( s * (s - side1) * (s - side2) * (s - side3) )**0.5
print("The area of the triangle is ", round(triangleArea, 2), ".")  # Print the triangle area out.
