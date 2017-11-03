#! /usr/bin/python -tt


'''
recursive function that calculates and returns exponatiation of base^exp
'''
import sys

def recur_power(base, exp):
    '''
    base: float or int
    exp: int >= 0
    returns base^exp
    '''

    if exp == 1:
        return base
    else:
        return base * recur_power(base, exp-1)


if len(sys.argv) > 2:
    base_this = int(sys.argv[1])
    exp_this = int(sys.argv[2])
    ans = recur_power(base_this, exp_this)
    print base_this, ' to the power of ', exp_this, ' = ',ans
else:
    base_this = 5
    exp_this  = 4
    ans = recur_power(base_this, exp_this)
    print base_this, ' to the power of ', exp_this, ' = ',ans
