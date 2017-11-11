#! /usr/bin/python -tt

"""itermul - iterative multiplication by successive addition"""

def itermul(multiply_this, by_this):
    result = 0
    for multiple in xrange(by_this):
        result = result + multiply_this
    return result

def itermul_gen(multiply_these):
    """Receives tuple from generator and returns the product"""
    print "Recived {} from test generators".format(multiply_these)
    multiply_this, by_this = multiply_these
    result = 0
    for multiple in xrange(by_this):
        result = result + multiply_this
    return result


def itermul_verify(verify_these):
    x, y = verify_these
    """Prints the test values and their comparison to returned values"""
    print '{} x {} should equal {}'.format(x, y, x*y)
    print '\n itermul({},{}) returned: {}'.format(x, y, itermul(x, y))
    if x * y == itermul_gen(verify_these):
        return 'PASS'
    else:
        return 'FAIL'

def test_generator(test_row):
    """Receives a test argument as tuple  from a genarator"""
    print 'generator delivers: {} and {}'.format(test_row[0], test_row[1])


if __name__ == '__main__':

    # Prep test values for a generator
    T = [[7, 3],
        [5, 6],
        [9, 1],
        [1001, 1111111]
        ]

    # Build generators to run itermul and its test function
    gen_itermul_test = (itermul_gen(test_row) for test_row in T)
    gen_itermul_verify = (itermul_verify(test_row) for test_row in T)

    # loops through the test value tuples and calls next for both test generators
    for i in T:
        print next(gen_itermul_test)
        print next(gen_itermul_verify)
