'''
Exercise05 - Sum Of Sequence Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 / n + sum(n - 1)


def main():
    print(sum(100))


main()
