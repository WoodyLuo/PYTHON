'''
Laboratory01 - Sorting Time.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''
import numpy as np
import time
import random
import sys

sys.setrecursionlimit(3000)

##### Bobble Sort #####
def BubbleSort(a_list):
	n = len(a_list)
	for i in range(0, n - 1):
		for j in range(i+1, n):
			if a_list[i] > a_list[j] :
				a_list[i], a_list[j] = a_list[j], a_list[i]
			# End if
		# End for loop
	# End for loop
# END of BubbleSort Function


##### Insertion Sort #####
def InsertionSort(a_list):
	n = len(a_list)
	for j in range(1, n):
		key = a_list[j]
		i = j - 1
		while i >= 0 and a_list[i] > key:
			a_list[i+1] = a_list[i]
			i = i - 1
		# End while loop
		a_list[i + 1] = key 
	# End for loop
# END of InsertionSort Function


##### Quick Sort #####
def QuickSort(a_list):

	def Partition(a_list, begin, end):
		# Always pick the end of element as the pivot
		pivot = a_list[end]
		# Initialize index of smaller element(indexSE = -1).
		indexSE = begin - 1 # index of smaller element
		for j in range(begin, end):
			''' Traverse element from j=begin to j=end. '''
			if a_list[j] <= pivot:
				# Increment index of smaller element.
				indexSE = indexSE + 1
				# If find a smaller element, we swap current-element(a_list[j]) with 'a_list[indexSE]'.
				a_list[indexSE], a_list[j] = a_list[j], a_list[indexSE]
			# End if
			# If a_list[j] > pivot, we do nothing.
		# To sort the pivot we swap a_list[indexSE+1] with a_list[end].
		a_list[indexSE+1], a_list[end] = a_list[end], a_list[indexSE+1]
		# End for loop
		# Return the index of sorted pivot. 
		return (indexSE+1)
	# END of Partition() Function

	def _quickSort(a_list, begin, end):
		''' Divide and conquer '''
		if begin < end:
			# Partition the array around pivot and recur for subarrays on left and right of pivot.
			partition_Index = Partition(a_list, begin, end)
			_quickSort(a_list, begin, partition_Index-1)
			_quickSort(a_list, partition_Index+1, end)
		else:
			# If begin >= end that means we had sort all element in a_list[]. Then return.
			return
		# End if...else...
	# END of _quickSort() function

	# Find the lenght of 'a_list[]'.
	n = len(a_list)
	_quickSort(a_list, 0, n-1)
# END of QuickSort() Function




#lst = [5, 3, 4, 6, 11, 9, 1, 0, -1, 7, 99, 43, 22, 10]
##### 1000 Numbers #####
n = 1000
lst = []
BS1000_Time = []
IS1000_Time = []
QS1000_Time = []
InnerQS1000_Time = []

print("Generating the data...")
for i in range(n):
	lst.append(random.randint(1,n))
lst4BS = lst.copy()
lst4IS = lst.copy()
lst4QS = lst.copy()
lst4InnerQS = lst.copy()
print("DONE - Generating the data")

print("Satrt to sort...")


print("Processing Bubble Sort (1000)...")
start = time.time()
BubbleSort(lst4BS)
end = time.time()
BS1000_Time.append(round(end - start, 2))
print("DONE - Processing Bubble Sort (1000).")

print("Processing Insertion Sort (1000)...")
start = time.time()
InsertionSort(lst4IS)
end = time.time()
IS1000_Time.append(round(end - start, 2))
print("DONE - Processing Insertion Sort (1000)...")

print("Processing Quick Sort (1000)...")
start = time.time()
QuickSort(lst4QS)
end = time.time()
QS1000_Time.append(round(end - start, 2))
print("DONE - Processing Quick Sort (1000)...")

print("Processing Inner Quick Sort (1000)...")
start = time.time()
lst4InnerQS.sort()
end = time.time()
InnerQS1000_Time.append(round(end - start, 2))
print("DONE - Processing Inner Quick Sort (1000)...")


##### 10,000 Numbers #####
n = 10000
lst = []

print("Generating the data...")
for i in range(n):
	lst.append(random.randint(1,n))
lst4BS = lst.copy()
lst4IS = lst.copy()
lst4QS = lst.copy()
lst4InnerQS = lst.copy()
print("DONE - Generating the data")

print("Satrt to sort...")

print("Processing Bubble Sort (10,000)...")
start = time.time()
BubbleSort(lst4BS)
end = time.time()
BS1000_Time.append(round(end - start, 2))
print("DONE - Processing Bubble Sort (10,000).")

print("Processing Insertion Sort (10,000)...")
start = time.time()
InsertionSort(lst4IS)
end = time.time()
IS1000_Time.append(round(end - start, 2))
print("DONE - Processing Insertion Sort (10,000)...")

print("Processing Quick Sort (10,000)...")
start = time.time()
QuickSort(lst4QS)
end = time.time()
QS1000_Time.append(round(end - start, 2))
print("DONE - Processing Quick Sort (10.000)...")

print("Processing Inner Quick Sort (10,000)...")
start = time.time()
lst4InnerQS.sort()
end = time.time()
InnerQS1000_Time.append(round(end - start, 2))
print("DONE - Processing Inner Quick Sort (10,000)...")


##### 100,000 Numbers #####
n = 100000
lst = []

print("Generating the data...")
for i in range(n):
	lst.append(random.randint(1,n))
lst4BS = lst.copy()
lst4IS = lst.copy()
lst4QS = lst.copy()
lst4InnerQS = lst.copy()
print("DONE - Generating the data")

print("Satrt to sort...")

print("Processing Bubble Sort (100,000)...")
start = time.time()
BubbleSort(lst4BS)
end = time.time()
BS1000_Time.append(round(end - start, 2))
print("DONE - Processing Bubble Sort (100,000).")

print("Processing Insertion Sort (100,000)...")
start = time.time()
InsertionSort(lst4IS)
end = time.time()
IS1000_Time.append(round(end - start, 2))
print("DONE - Processing Insertion Sort (100,000)...")

print("Processing Quick Sort (100,000)...")
start = time.time()
QuickSort(lst4QS)
end = time.time()
QS1000_Time.append(round(end - start, 2))
print("DONE - Processing Quick Sort (100,000)...")

print("Processing Inner Quick Sort (100,000)...")
start = time.time()
lst4InnerQS.sort()
end = time.time()
InnerQS1000_Time.append(round(end - start, 2))
print("DONE - Processing Inner Quick Sort (100,000)...")


print("   輸入資料(n)   | 1,000 | 10,000 | 100,000")
print("   BubbleSort    |", format(BS1000_Time[0], '.2f'), " |", format(BS1000_Time[1], '.2f'), "  |", format(BS1000_Time[2], '.2f') )
print("  InsertionSort  |", format(IS1000_Time[0], '.2f'), " |", format(IS1000_Time[1], '.2f'), "  |", format(IS1000_Time[2], '.2f') )
print("   QuickSort     |", format(QS1000_Time[0], '.2f'), " |", format(QS1000_Time[1], '.2f'), "  |", format(QS1000_Time[2], '.2f') )
print("    內建Sort     |", format(InnerQS1000_Time[0], '.2f'), " |", format(InnerQS1000_Time[0], '.2f'), "  |", format(InnerQS1000_Time[0], '.2f'), )

