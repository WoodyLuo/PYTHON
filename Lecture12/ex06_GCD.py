'''
Exercise06 - GCD Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


def main():
    m = eval(input("Enter m:"))
    n = eval(input("Enter n:"))
    print(gcd(m, n))


main()
