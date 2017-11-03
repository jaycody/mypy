#! /usr/bin/python -tt

'''
Uses iteration (rather than recursion) to
caculate and return the n-bang for a given interger n.
n! = n * (n-1)!
'''
import sys

def n_bang_iterative(n):

    factorial_of = n
    result = n
    countdown = 1
    n = n-1

    while n > 1:
        print 'on iteration', countdown, ':   ', factorial_of, 'Factorial = ', result, ' * ', str(n),'Factorial', '\n'
        result = result * (n)
        n = n-1
        countdown = countdown +1
    print 'on iteration', countdown, ':   ', factorial_of, 'Factorial = ', result, ' * ', n, '\n'
    return result


if len(sys.argv) > 1:
    factorial_this = int(sys.argv[1])
    ans = n_bang_iterative(factorial_this)
    print factorial_this, 'Factorial = ', ans
else:
    factorial_this = 50
    ans = n_bang_iterative(factorial_this)
    print factorial_this, 'Factorial = ', ans
