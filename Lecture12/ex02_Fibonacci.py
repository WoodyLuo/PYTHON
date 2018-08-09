'''
Exercise02 - Fibonacci Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    index = eval(input("Enter an index for a Fibonacci number: "))
    print("The Fibonacci number at index", index, "is", fib(index))


main()
