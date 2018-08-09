'''
Exercise01 - Bubble Sort Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def BubbleSort(a):
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


lst = [5, 2, 4, 6, 1, 3]
BubbleSort(lst)
print(lst)
