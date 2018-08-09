'''
Exercise05 - GCDFunction Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def gcd(n1, n2):
    gcd = 1
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return gcd


def main():
    n1 = eval(input("Enter the first integer:"))
    n2 = eval(input("Enter the second integer:"))
    print("The greatest common divisor for", n1, "and", n2, "is", gcd(n1, n2))


main()
