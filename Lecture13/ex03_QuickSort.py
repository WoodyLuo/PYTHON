'''
Exercise03 - Quick Sort.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''


def Partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x :
			i = i + 1
			A[i], A[j] = A[j], A[i]
		# End if
	# End for loop
	A[i+1], A[r] = A[r], A[i+1]
	return (i + 1)
# END of Partition() Function

def quickSort(A, p, r):
	if p<r:
		q = Partition(A, p, r)
		quickSort(A, p, q-1)
		quickSort(A, p+1, r)
	# End if
# END of quickSort() Function


def QuickSort(A):
	n = len(A)
	quickSort(A, 0, n-1)
# END of quickSort() Function


lst = [5, 3, 4, 6, 11, 9, 1, 0, -1, 7, 99, 43, 22, 10]
print("Original list arrray:", lst)
QuickSort(lst)
print("Sorted list arrray:", lst)

