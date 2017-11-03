#! /usr/bin/python -tt

'''
recursive function that calculates and returns n-bang
'''

import sys

def n_bang_recursive(n):
    '''
    assumes n is an int > 0
    returns n!
    '''
    #base case
    if n == 1:
        return n
    # recursive step
    else:
        return n * n_bang_recursive(n-1)



if len(sys.argv) > 1:
    factorial_this = int(sys.argv[1])
    ans = n_bang_recursive(factorial_this)
    print factorial_this, 'Factorial = ', ans
else:
    factorial_this = 500
    ans = n_bang_recursive(factorial_this)
    print factorial_this, 'Factorial = ', ans
