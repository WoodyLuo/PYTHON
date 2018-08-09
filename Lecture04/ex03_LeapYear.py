'''
Exercise03 - LeapYear Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

year = eval(input("Enter a year:"))
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 != 0) or (year % 400 == 0)
print(year, "is a leap year?", isLeapYear)
input()
