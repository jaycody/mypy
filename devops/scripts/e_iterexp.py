#! usr/bin/python -tt

'''
Iterative function that calculates the exponential base^exp by successively adding
the result of a secondary function that calculates the product of two values by 
successively adding one value to itself.
'''


import sys

def iterexp(base, exp):
    '''
    base: int or float
    exp: int >= 0

    returns: int or float, base^exp
    '''

    results_from_iterexp = 0
    for i in xrange(exp):
        results_from_iterexp = itermul(base, base) + results_from_iterexp
    return results_from_iterexp


def itermul(add_this_to_itself, this_many_times):
    '''
    iterative multiplication via successive addition
    For each of the exp loops in the iterexp function, a call is made to the itermul function
    such that successive addition is used to find a product, and successive calls to this function are used to caclulate an exponent via successive multiplication
    '''
 
    results_from_itermul = 0
    for i in xrange(this_many_times):
        results_from_itermul = add_this_to_itself + results_from_itermul
    return results_from_itermul
        

if len(sys.argv) == 3:
    final_result = iterexp(int(sys.argv[1]), int(sys.argv[2]))
else:
    final_result = iterexp(3, 3)

print final_result
