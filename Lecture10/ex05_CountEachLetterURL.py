'''
Exercise05 - Count Each Letter URL Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import urllib.request


def main():
    url = input("Enter an URL for a file:").strip()
    infile = urllib.request.urlopen(url)
    s = infile.read().decode()
    counts = countLetters(s.lower())
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i), "appears", str(counts[i]), ("time"if counts[i] == 1 else "times"))


def countLetters(s):
    counts = 26 * [0]
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts


main()
