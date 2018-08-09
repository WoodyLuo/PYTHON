'''
Exercise05 - HarmonicSeries Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

a = 0
b = 0
for i in range(1, 50001):
	a += 1 / i
print("leftAdd:", a)
for i in range(50000, 0, -1):
	b += 1 / i
print("rightAdd:", b)
input()
