'''
Exercise02 - Binary Search Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
    return -1


def main():
    lst = [2, 4, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79]
    i = binarySearch(lst, 4)
    j = binarySearch(lst, 66)
    k = binarySearch(lst, 53)
    print("i =", i)
    print("j =", j)
    print("k =", k)


main()
