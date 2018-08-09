'''
Exercise04 - Equation Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import math

a, b, c = eval(input("Enter a, b, c:"))
expression = b * b - 4 * a * c
if expression > 0:
    r1 = (-b + math.sqrt(expression)) / 2 * a
    r2 = (-b - math.sqrt(expression)) / 2 * a
    print("The root is", r1, "and", r2)
elif expression == 0:
    r1 = (-b + math.sqrt(expression)) / 2 * a
    print("The root is", r1)
else:
    print("The equation has no real roots")
input()
