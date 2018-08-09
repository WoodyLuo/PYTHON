'''
Exercise05 - Tic Tac Toe Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
k = 0
for i in range(4):
    print("-------------")
    for j in range(4):
        if j == 3:
            print("|")
        elif i == 3:
            break
        else:
            print("| " + lst[i][j] + " ", end='')
while k < 9:
    try:
        if k % 2 == 0:
            row = eval(input("Enter a row (0, 1, 2) for player X:"))
            column = eval(input("Enter a column (0, 1, 2) for player X:"))
            if lst[row][column] == 'X' or lst[row][column] == 'O':
                print("Input error.")
            else:
                lst[row][column] = 'X'
        else:
            row = eval(input("Enter a row (0, 1, 2) for player O:"))
            column = eval(input("Enter a column (0, 1, 2) for player O:"))
            if lst[row][column] == 'X' or lst[row][column] == 'O':
                print("Input error.")
            else:
                lst[row][column] = 'O'
        for i in range(4):
            print("-------------")
            for j in range(4):
                if j == 3:
                    print("|")
                elif i == 3:
                    break
                else:
                    print("| " + lst[i][j] + " ", end='')
        if lst[0][0] == lst[0][1] == lst[0][2] != ' ' or \
           lst[1][0] == lst[1][1] == lst[1][2] != ' ' or \
           lst[2][0] == lst[2][1] == lst[2][2] != ' ' or \
           lst[0][0] == lst[1][0] == lst[2][0] != ' ' or \
           lst[0][1] == lst[1][1] == lst[2][1] != ' ' or \
           lst[0][2] == lst[1][2] == lst[2][2] != ' ' or \
           lst[0][0] == lst[1][1] == lst[2][2] != ' ' or \
           lst[0][2] == lst[1][1] == lst[2][0] != ' ':
            print(lst[row][column], "player won.")
            break
        else:
            if k == 8:
                print("It is a draw.")
        k += 1
    except:
        print("Input error.")




