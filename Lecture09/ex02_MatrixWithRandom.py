'''
Exercise02 - Matrix with random Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import random
matrix = []
numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))
for row in range(numberOfRows):
    matrix.append([])  # add an empty new row
    for column in range(numberOfColumns):
        matrix[row].append(random.randint(0, 99))
print(matrix)
