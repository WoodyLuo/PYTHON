'''
Exercise04 - PrimeNumber Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def isPrime(number):
	divisor = 2
	while divisor <= number / 2:
		if number % divisor == 0:
			return False
		divisor += 1
	return True


def main():
	NUMBER_OF_PRIMES = 50
	NUMBER_OF_PRIMES_PER_LINE = 10
	count = 0  # count the number of prime numbers
	number = 2  # number to be tested if prime
	print("The first 50 prime numbers are" )
	while count < NUMBER_OF_PRIMES :
		if isPrime(number):
			print(format(number, "5d"), end=' ')
			count += 1
			if count % NUMBER_OF_PRIMES_PER_LINE == 0:
				print()
		number += 1


main()
input()
