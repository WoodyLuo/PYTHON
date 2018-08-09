'''
Exercise01 - Recursion Binomial Coefficient & Looping Binomial Coefficient

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
REFERENCE: www.geeksforgeeks.org
'''
import time


# A naive recursive Python implementation.
def binomial_recursion(n, k):
	if k==0 or n==k:
		return 1
	else:
		# Recursive Call
		return binomial_recursion(n-1, k) + binomial_recursion(n-1, k-1)
	# End if...else...
# END of binomial_recursion Function.



def binomial_loop(n, k):

	memo = [ [0 for x in range(k+1)] for x in range(n+1) ]

	# Calculate value of Binomial Coefficient in bottom up manner.
	for i in range(n+1):
		for j in range(min(i,k)+1):
			# Base Cases
			if j==0 or j==i:
				memo[i][j] = 1
			
			# Calculate value using Previosly stored values.
			else:
				memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
			# End if...else
		# End loop
	#End loop
	return memo[n][k]
# Time Complexity: O(n*k)
# Auxiliary Space: O(n*k)
# END of binomial_loop Function.


def main():

	start = time.time()
	print(binomial_recursion(35,6))
	end = time.time()
	print("Spanding time of recursion binomial is:", format(end-start, '.3f'))
	
	start = time.time()
	print(binomial_loop(35,6))
	end = time.time()
	print("Spanding time of loop binomial is:", format(end-start, '.3f'))


main()