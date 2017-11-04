#! /usr/bin/python -tt

'''
Calculates Greatest Common Divisor
- using Euclid's Algorithm
- expressed as a recursive function
- in Python
'''

def euclid(a, b):
    '''
    assume a and b are positive integers

    if b is False : returns b
    if b is True  : returns either euclid(b, a % b) or a

    if b is True and if euclid(b, a % b) is True    : returns eudlid(b, a % b)
    if b is True and if euclid(b, a % b) if False   : returns a

    Under what conditions would euclid(b, a % b) evaluate to false?
            ans: when b divides into 'a' evenly leaving no remainder
                   ie, when a % b == 0
    '''

    return b and euclid(b, a % b) or a



print euclid(40, 10)
