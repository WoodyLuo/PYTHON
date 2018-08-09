'''
Laboratory01 - Recursive Euler Algorithm & Recursive Harmonic Series.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''


def harmonic_sum(n):
	if n<2:
		return 1
	else:
		return 1/n + (harmonic_sum(n-1))
	# End if...else...
# END of harmonic_sum() Function


def gcd(a, b):
	"""
	Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
	"""
	if b > a:
		return gcd(b, a)
	# End if
	if a % b == 0:
		return b
	# End if
	return gcd(b, a%b)
# END of gcd() Function


def main():
	for i in range(1, 100+1):
		''' print Harmonic Sum 1 to 100. '''
		print("Harmonic Sum (m(%i))" %i, harmonic_sum(i))

	m = eval(input("Please, enter the value of m "))
	n = eval(input("Please, enter the value of n "))
	print("The greatest common divisor of {0} and {1} is \"".format(m, n) , gcd(m, n), "\"")

main()

