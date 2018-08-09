'''
Exercise05 - HarmonicSeries Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import numpy as np

n1 = input("Enter number:")
'''
Exercise04 - Compute matrix Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

matrix1 = np.array(n1.split(" "), dtype=float).reshape(3, 3)

n2 = input("Enter number:")
matrix2 = np.array(n2.split(" "), dtype=float).reshape(3, 3)

matrix3 = matrix1 + matrix2
matrix4 = np.dot(matrix1, matrix2)

matrix5 = np.hstack((np.hstack((matrix1, matrix2)), matrix3))
matrix6 = np.hstack((np.hstack((matrix1, matrix2)), matrix4))

print("The matrices are added as follows:")
for i in range(3):
    for j in range(9):
        if j == 8:
            print(format(str('%.1f' % matrix5[i][j]), '<4s'))
        elif i == 1 and j == 2:
            print(format(str('%.1f' % matrix5[i][j]), '<4s'), "+  ", end='')
        elif i == 1 and j == 5:
            print(format(str('%.1f' % matrix5[i][j]), '<4s'), "=  ", end='')
        else:
            print(format(str('%.1f' % matrix5[i][j]), '<4s'), "   ", end='')
print()
print("The multiplication of the matrices is:")
for i in range(3):
    for j in range(9):
        if j == 8:
            print(format(str('%.1f' % matrix6[i][j]), '<4s'))
        elif i == 1 and j == 2:
            print(format(str('%.1f' % matrix6[i][j]), '<4s'), "*  ", end='')
        elif i == 1 and j == 5:
            print(format(str('%.1f' % matrix6[i][j]), '<4s'), "=  ", end='')
        else:
            print(format(str('%.1f' % matrix6[i][j]), '<4s'), "   ", end='')
