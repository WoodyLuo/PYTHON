'''
Exercise05 - ScissorRockPaper Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import random

a = eval(input("scissor(0), rock(1), paper(2):"))
x = random.randint(0, 2)

if x == 0:
    if a == 0:
        print("The computer is scissor. You are scissor too. It is a draw.")
    elif a == 1:
        print("The computer is scissor. You are rock. You won.")
    else:
        print("The computer is scissor. You are paper. You loss.")
elif x == 1:
    if a == 0:
        print("The computer is rock. You are scissor too. You loss.")
    elif a == 1:
        print("The computer is rock. You are rock too. It is a draw.")
    else:
        print("The computer is rock. You are paper. You win.")
else:
    if a == 0:
        print("The computer is paper. You are scissor. You win.")
    elif a == 1:
        print("The computer is paper. You are rock. You loss.")
    else:
        print("The computer is paper. You are paper too. It is a draw.")
input()
