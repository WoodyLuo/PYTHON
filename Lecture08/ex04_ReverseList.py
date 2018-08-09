'''
Exercise04 - ReverseList Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def reverse(lst):
    result = []
    for element in lst:
        result.insert(0, element)
    return result


list1 = [1, 2, 3, 4, 5]
list2 = reverse(list1)
print("list1 =", list1)
print("list2 =", list2)
