#! /usr/bin/python -tt

'''
Recursively calculate the GREATEST COMMON DIVISOR

...where the GCD of two positive integers is the largest integer that
divides each them without a remainder

steps:
1. Pick a candidate divisor equal to the smallest of the two integers.
2. Divide both integers by the candidate gcd and check for a remainder.
3. If no remainder in either case, then candidate == gcd
4. If remainder exists for either case, reduce the candidate divisor by 1 and retest.
5. Continue testing for zero remainder until success or candidate reduces to 1
'''

import sys

def gcd_iter(a, b):
    candidate_divisor = min(a, b)
    while candidate_divisor >= 1:
        if candidate_divisor == 1:
            return candidate_divisor
        if (a % candidate_divisor == 0) and (b % candidate_divisor == 0):
            return candidate_divisor
        else:
            candidate_divisor = candidate_divisor -1


if len(sys.argv) > 2:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    ans = gcd_iter(a, b)
    print ans, 'is the Greatest Common Divisor of', a, 'and',b
else:
    a = 9
    b  = 12
    ans = gcd_iter(a, b)
    print ans, 'is the Greatest Common Divisor of', a, 'and',b
