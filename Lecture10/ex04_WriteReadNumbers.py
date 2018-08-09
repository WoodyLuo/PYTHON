'''
Exercise04 - Write Read Numbers Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

from random import randint


def main():
    outfile = open("Numbers.txt", "w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close()
    infile = open("Numbers.txt", "r")
    s = infile.read()
    numbers = [eval(x)for x in s.split()]
    for number in numbers:
        print(number, end='')
    infile.close()


main()
