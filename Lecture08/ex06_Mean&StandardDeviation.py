'''
Exercise06 - Mean and Standard Deviation Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def mean(x):
    a = 0
    for i in range(len(x)):
        try:
            a += int(x[i])
        except:
            a += float(x[i])
    m = a / len(x)
    return m


def std(x):
    a = 0
    for j in range(len(x)):
        try:
            a += ((int(x[j]) - mean(x)) ** 2)
        except:
            a += ((float(x[j]) - mean(x)) ** 2)
    s = (a / (len(x) - 1)) ** 0.5
    return s


def main():
    n = input("Enter number:")
    x = n.split()
    print("The mean is", round(mean(x), 2))
    print("The standard deviation is", round(std(x), 5))


main()
