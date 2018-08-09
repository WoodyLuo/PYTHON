'''
Exercise01 - Linear Search Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def lineSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1


def main():
    lst = [1, 4, 4, 2, 5, -3, 6, 2]
    i = lineSearch(lst, 4)
    j = lineSearch(lst, -4)
    k = lineSearch(lst, -3)
    print("i =", i)
    print("j =", j)
    print("k =", k)


main()
