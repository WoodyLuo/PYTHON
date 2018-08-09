'''
Exercise01 - GuessNumber Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import random
number = random.randint(1, 100)
print("Guess a magic number between 0 to 100")
guess = -1
while guess != number:
	guess = eval(input("Enter your guess:"))
	if guess == number:
		print("Yes, the number is", number)
	elif guess > number:
		print("Your guess is too high")
	else:
		print("Your guess is too low")
input()
