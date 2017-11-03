#! /usr/bin/python -tt

"""itermul - interative multiplication by successive addition"""



def itermul(multiply_this, by_this):
    result = 0
    for multiple in xrange(by_this):
        result = result + multiply_this
    return result


print itermul(7, 3)
