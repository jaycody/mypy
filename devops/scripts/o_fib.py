#! /usr/bin/python -tt

'''
Calculates Fibonacci numbers for any positive int
'''

def fib(n):
    # check type

    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    else:
        print n 
        return fib(n-1) + fib(n-2)





print fib(10)
