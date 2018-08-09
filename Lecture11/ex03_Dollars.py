'''
Exercise03 - Dollars Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

dollars = eval(input("Enter the change:"))

oneThousand = dollars // 1000
fiveHundred = (dollars % 1000) // 500
oneHundred = (dollars % 1000 % 500) // 100
fifty = (dollars % 1000 % 500 % 100) // 50
ten = (dollars % 1000 % 500 % 100 % 50) // 10
five = (dollars % 1000 % 500 % 100 % 50 % 10) // 5
one = (dollars % 1000 % 500 % 100 % 50 % 10 % 5) // 1

print("1000 dollars", oneThousand)
print("500 dollars", fiveHundred)
print("100 dollars", oneHundred)
print("50 dollars", fifty)
print("10 dollars", ten)
print("5 dollars", five)
print("1 dollars", one)
