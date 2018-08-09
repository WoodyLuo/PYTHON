'''
Exercise08 - TestRactangle Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

from Lecture7_Rectangle import Rectangle


def main():
    r1 = Rectangle(4, 40)
    r2 = Rectangle(3.5, 35.7)
    print(r1.width, r1.height, r1.getArea(), r1.getPerimeter())
    print(r2.width, r2.height, r2.getArea(), r2.getPerimeter())


main()
