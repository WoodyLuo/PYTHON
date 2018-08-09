'''
Exercise01 - list Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

list1 = []  # list1 = list()
list2 = [1, 2, 3, 4, 5, 6, 7]  # list2 = list([1, 2, 3, 4, 5, 6, 7])
list3 = ["red", "green", "blue"]  # list3 = list(["red", "green", "blue"])
list4 = [*range(3, 8)]  # list4 = list(range(3, 8))
print(list1)
print(list2)
print(list3)
print(list4)

list5 = [4, 7, 9, 2, 6, 1, 5, 3]
print(3 in list5)  # result = True
print(8 in list5)  # result = False
print(max(list5))  # result = 9
print(min(list5))  # result = 1
print(sum(list5))  # result = 37
print(list5[3])  # result = 2
print(list5[2:4])  # result = [9, 2]
print(list5[:2])  # result = [4, 7]
print(list5[4:])  # result = [6, 1, 5, 3]

list5.append(9)
list5.insert(1, 6)
print(list5)  # result = [4, 6, 7, 9, 2, 6, 1, 5, 3, 9]
print(list5.count(4))  # result = 1
print(list5.index(4))  # result = 0

list6 = [1, 5]
list7 = [7, 3]

print(list6 + list7)  # result = [1, 5, 7, 3]
print(list6 * 3)  # result = [1, 5, 1, 5, 1, 5]

list8 = [1, 3, 5, 7, 9]
# three of method copy list8
list9 = list8
list10 = [x for x in list8]
list11 = [] + list8
print(list8)
print(list9)
print(list10)
print(list11)
