'''
Exercise01 - PrintGradeFunction Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def printGrade(score):
	if score >= 90.0:
		print('A')
	elif score >= 80.0:
		print('B')
	elif score >= 70.0:
		print('C')
	elif score >= 60.0:
		print('D')
	else :
		print('F')


def main():
	score = eval(input("Enter a score : "))
	print("The grade is ", end=' ')
	printGrade(score)


main()
input()
