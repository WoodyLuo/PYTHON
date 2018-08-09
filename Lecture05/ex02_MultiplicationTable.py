'''
Exercise02 - MultiplicationTable Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

print("            Multiplication Table")
print()
print("   |", end='')
for j in range(1, 10):
	print(format(j, '4d'), end='')
print()
print("-------------------------------------------")
for i in range(1, 10):
	print(i, " |", end='')
	for j in range(1, 10):
		print(format(i * j, '4d'), end='')
	print()
input()
