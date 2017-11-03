#! /usr/bin/python -tt



'''
recursive function that returns the product of two multipliers
'''

import sys

def recur_mul(multiply_this, this_many_times):
    print 'here again?'
    
    # base case
    if this_many_times == 1:
        return multiply_this

    # recursive step
    else:
        return multiply_this + recur_mul(multiply_this, this_many_times - 1)

if len(sys.argv) > 2:
    print recur_mul(int(sys.argv[1]), int(sys.argv[2]))
else:
    print recur_mul(3, 5)
