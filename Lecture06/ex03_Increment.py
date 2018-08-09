'''
Exercise03 - Increment Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def increment(n):
	n += 1
	print("\t n inside the function is", n)


def main():
	x = 1
	print("Before the call, x is", x)
	increment(x)
	print("After the call, x is", x)


main()
input()
