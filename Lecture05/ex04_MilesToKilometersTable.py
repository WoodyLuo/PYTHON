'''
Exercise04 - Miles to Kilometers Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

print("Miles      Kilometers")
print()
for i in range(1, 11):
	print(format(i, '<10d'), "%.3f" % (i*1.609))
input()
