'''
Exercise07 - Rectangle Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getArea(self):
        return self.width * self.height

    def setWidthHeight(self, width, height):
        self.width = width
        self.height = height
