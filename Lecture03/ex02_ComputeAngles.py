'''
Exercise02 - Compute Angles.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''
import math

# Three points is: 1.0, 1.0, 6.5, 1.0, 6.5, 2.5
# Three angle is: 15.26, 90.0, 74.74
x1, y1, x2, y2, x3, y3 = eval( input("Enter three points: ") )

a = math.sqrt( (x2-x3)*(x2-x3)+(y2-y3)*(y2-y3) )
b = math.sqrt( (x1-x3)*(x1-x3)+(y1-y3)*(y1-y3) )
c = math.sqrt( (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2) )

A = math.degrees( math.acos( (a*a-b*b-c*c)/(-2*b*c) ) )
B = math.degrees( math.acos( (b*b-a*a-c*c)/(-2*a*c) ) )
C = math.degrees( math.acos( (c*c-b*b-a*a)/(-2*a*b) ) )

print( "The three angles are", round(A*100)/100.0, round(B*100)/100.0, round(C*100)/100.0 )
