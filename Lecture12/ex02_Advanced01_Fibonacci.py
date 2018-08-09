'''
Exercise01 - (Recursion) Fibonacc & (Dynamic Programming) Fibonacc

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
REFERENCE: www.geeksforgeeks.org
'''
import time


# Fibonacci Series using Recursion.
def fibonacci_R(n):

	if  n < 0:
		print("Incorrect input!")
	# First Fibonacci number is 0
	elif n == 0:
		return 0
	# Second Fibonacci number is 1
	elif n == 1 or n == 2:
		return 1
	else:
		return fibonacci_R(n - 1) + fibonacci_R(n - 2)
	# End of if... else if... else..
# Time Complexity: T(n) = T(n-1) + T(n-2) = O(2n)
# Extra Space: O(n)
#END of fibonacci_R() Function


# Fibonacci Series using Dynamic Programming.
def fibonacci_DP(n):
	''' Storing the Fibonacci numbers calculated so far. So we can aviod the repeated work done. '''
	# Taking list[] two fibonacci numbers as 0 and 1.
	a = 0
	b = 1

	if n < 0:
		print("Incorrect Input!")
	elif n == 0:
		return a

	elif n == 1:
		return b

	else:
		for i in range(2, n+1):
			c = a + b
			a = b
			b = c
		return b 
	# End if... else...

# Time Complexity: O(n)
# Extra Space: O(1)
#END of fibonacci_DP() Function


def main():
	
	index = eval(input("Enter an index for a Fibonacci number: "))
	start = time.time()
	print( "The Fibonacci number at index", index, "is", fibonacci_R(index) )
	end = time.time()
	print( "Recursion Fibonacci number is:", format(end-start, '.3f') )

	start = time.time()
	print( "The Fibonacci number at index", index, "is", fibonacci_DP(index) )
	end = time.time()
	print( "Dynamic Frogramming Fibonacci number is:", format(end-start, '.3f') )


main()
