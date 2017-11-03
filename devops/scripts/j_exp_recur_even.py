#! /usr/bin/python -tt


'''
recursively calculates base^exp

uses two solutions, one for even and one for odd exponents

if exp is even: then base^exp = (base^2)^(exp/2)
if exp is odd: then base^exp = base * base^(exp-1)

'''
import sys

def recur_power_new(base, exp):
    if exp == 1:
        return base

    # odd case
    if exp % 2 == 1:
        return base * recur_power_new(base, exp-1)
    else:
        return recur_power_new(base * base, exp/2)


#print recur_power_new(5, 2)




if len(sys.argv) > 2:
    base_this = int(sys.argv[1])
    exp_this = int(sys.argv[2])
    ans = recur_power_new(base_this, exp_this)
    print base_this, ' to the power of ', exp_this, ' = ',ans
else:
    base_this = 5
    exp_this  = 2
    ans = recur_power_new(base_this, exp_this)
    print base_this, ' to the power of ', exp_this, ' = ',ans
