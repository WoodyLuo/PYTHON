'''
Exercise02 - TestCircle Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

from Lecture7_Circle import Circle


def main():
    circle1 = Circle()
    print("The area of the circle of radius", circle1.radius, "is", circle1.getArea())
    circle2 = Circle(25)
    print("The area of the circle of radius", circle2.radius, "is", circle2.getArea())
    circle3 = Circle(125)
    print("The area of the circle of radius", circle3.radius, "is", circle3.getArea())


main()
