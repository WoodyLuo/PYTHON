'''
Laboratory02 - Compute Polygon Area.
Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''
import math

numSide = eval( input("Enter the number of sides:") )
sideLength = eval( input("Enter the side of length:") )

polygonArea = (numSide*sideLength**2) / (4*math.tan(math.pi/numSide))
print("The area of the polygon is ", polygonArea)