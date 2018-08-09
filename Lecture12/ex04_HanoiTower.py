'''
Exercise04 - HanoiTower Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def HanoiTower(A, B, C, n):
    if n == 1:
        print("Move from", A, "to", C)
    else:
        HanoiTower(A, C, B, n - 1)
        HanoiTower(A, B, C, 1)
        HanoiTower(B, A, C, n - 1)


def main():
    HanoiTower("A", "B", "C", 15)


main()
