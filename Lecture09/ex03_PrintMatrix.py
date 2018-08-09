'''
Exercise03 - Print matrix Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column], end='')
    print()

print()

for row in matrix:
    for value in row:
        print(value, end='')
    print()
