'''
Exercise01 - Binomial Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def binomial(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return binomial(n - 1, k) + binomial(n - 1, k - 1)


def main():
    print(binomial(5, 3))


main()