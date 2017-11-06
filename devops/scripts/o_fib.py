#! /usr/bin/python -tt

'''
Calculates Fibonacci numbers for any positive int
'''

def fib(n):
    '''
    expects a postive int
    '''
    
    # assert positive int
    assert type(n)==int and n >= 0

    # Base Case
    if n == 0 or n == 1:
        return 1

    # Recursive Case
    else:
        return fib(n-1) + fib(n-2)

for i in xrange(20):
    print "For round: " + str(i) + '  Fibonacci=' + str(fib(i))
