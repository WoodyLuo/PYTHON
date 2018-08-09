'''
Exercise02 - Insertion Sort Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def InsertionSort(a):
    n = len(a)
    for j in range(1, n):
       key = a[j]
       i = j - 1
       while i >= 0 and a[i] > key:
           a[i+1] = a[i]
           i = i - 1
       a[i+1] = key


lst = [5, 2, 4, 6, 1, 3]
InsertionSort(lst)
print(lst)
