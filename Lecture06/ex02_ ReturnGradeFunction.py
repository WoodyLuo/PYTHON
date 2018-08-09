'''
Exercise02 - ReturnGradeFunction Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def getGrade(score):
	if score >= 90.0:
		return 'A'
	elif score >= 80.0:
		return 'B'
	elif score >= 70.0:
		return 'C'
	elif score >= 60:
		return 'D'
	else:
		return 'F'


def main():
	score = eval(input("Enter a score : "))
	print("The grade is", getGrade(score))


main()
input()
