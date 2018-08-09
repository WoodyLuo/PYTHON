'''
Exercise03 - Copy file Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import sys
import os


def main():
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()
    if os.path.isfile(f2):
        print(f2 + " already exists")
        sys.exit()
    infile = open(f1, "w")
    infile.write("Bill Clinton\n")
    infile.write("George Bush\n")
    infile.write("Barack Obama")
    infile.close()
    infile = open(f1, "r")
    outfile = open(f2, "w")
    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines, "lines and", countChars, "chars opied")
    infile.close()
    outfile.close()


main()
