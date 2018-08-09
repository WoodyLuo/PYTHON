'''
Exercise06 - TestCircleWithPrivateRadius Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

from Lecture7_CircleWithPrivateRadius import Circle


def main():
    circle1 = Circle()
    print("The area of the circle of radius", circle1.getRadius(), "is", circle1.getArea())
    circle2 = Circle(25)
    print("The area of the circle of radius", circle2.getRadius(), "is", circle2.getArea())
    circle3 = Circle(125)
    print("The area of the circle of radius", circle3.getRadius(), "is", circle3.getArea())


main()
