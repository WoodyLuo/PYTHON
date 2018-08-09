'''
Laboratory01 - Sine Function And Output The Text File For Sine Function.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''
import math


def dRange(start, end, step):
	''' Genetate points in list. '''
	TO_RETURN = []
	if start < end:
		i = start
		n = end
		while i <= n:
			TO_RETURN = TO_RETURN + [i]
			i = i + step
		# End while loop
	else:
		i = start
		n = end
		while i >= n:
			TO_RETURN = TO_RETURN + [i]
			i = i - abs(step)
		# End while loop
	# End if...else...

	return TO_RETURN
#END of dRange() Function

def main():
	a_cycle = dRange(0.0, 2*math.pi, 0.1)  # Generate the data points.
	a_sin = a_cycle.copy()                 # Copy the list array (a_cycle).
	
	fileName = "Output_SineFuntion.txt"
	with open(fileName, 'w') as file_Obj:

		for i in range(len(a_sin)):
			a_cycle[i] = round(a_cycle[i], 2)
			a_sin[i] = round(math.sin(a_sin[i]), 4)
			file_Obj.write(str(a_cycle[i])+"    "+str(a_sin[i])+'\n')
		# End for loop

	print(a_cycle)  # Print the sample points for sine function.
	print(a_sin)    # Print the values of sine.
#END of main() function


def plotSin():
	''' Plot thr sine function using 'matplotlib' package. '''
	import matplotlib.pyplot as plt
	plt.plot(a_cycle, a_sin, label='Sin()')
	plt.legend()
	plt.show()

main()

