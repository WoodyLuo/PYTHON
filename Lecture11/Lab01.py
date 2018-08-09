'''
Laboratory01 - Make Change.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''
debugMode = False


def makeChange(amount, currency):
	# initialize arrays for $0
	minimum_number_of_currency = [0]
	currency_composition = [[]]
	number_of_50dollars = 0
	number_of_10dollars = 0
	number_of_5dollars = 0
	number_of_1dollars = 0

	for i in range(1, amount+1):
		best = 10000
		best_currency_composition = None

		for j in currency:
			if i-j > -1  and  minimum_number_of_currency[i-j]+1 < best:
				best = minimum_number_of_currency[i-j]+1
				best_currency_composition = currency_composition[i-j] + [j]
			# End if

		minimum_number_of_currency.append(best)
		currency_composition.append(best_currency_composition)
		if debugMode == True:
			print('{0:3} {1} {2}'.format(i, best, best_currency_composition))
		# End if
		# End for loop
	# Enf for loop

	for k in range(len(best_currency_composition)):
		if best_currency_composition[k] == 50 :
			number_of_50dollars = number_of_50dollars + 1
		elif best_currency_composition[k] == 10:
			number_of_10dollars = number_of_10dollars + 1
		elif best_currency_composition[k] == 5:
			number_of_5dollars = number_of_5dollars + 1
		else:
			number_of_1dollars = number_of_1dollars + 1

	return best_currency_composition, best, number_of_50dollars, number_of_10dollars, number_of_5dollars, number_of_1dollars
# END of makeChange() Function.


# USD - $1, $5, $10, $50, $100
# NTD - $1, $5, $10, $50, $100, $200, $500, $1000, $2000
currency = [1, 5, 10, 50]

# The amount to change = ??
amount = eval( input("Enter the change:") )

best_currency_composition, totalCoinsNum, Num50D, Num10D, Num5D, Num1D = makeChange(amount, currency)

print("50 dollars", Num50D)
print("10 dollars", Num10D)
print("5  dollars", Num5D)
print("1  dollars", Num1D)
print("Total coins number: ", totalCoinsNum)

