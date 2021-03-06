#! /usr/bin/python -tt

""" Guardian of the function threshold"""

def check_this(x):
    """Returns None if value is anything other than a positive int"""

    if not isinstance(x, int):
        return None, x

    if x < 0:
        return None, x

    return 'PASS', 'input: {} is a positive integer'.format(x)


def test_check_this(val_to_check):
    """Compares check_this function's results with expected"""

    print '\nChecking input: {} ----->'.format(val_to_check)
    results = check_this(val_to_check)

    ## if PASS
    if results[0] is not None:
        return results

    ## if negative
    elif results[1] < 0:
        return '\tNope! {} is as negative as Julian in Less Than Zero'.format(results[1])

    ## if NOT INT
    else:
        return '\tNope! Input: {} is of type: {}'.format(val_to_check, type(val_to_check))

if __name__ == '__main__':

    ## GENERATOR runs each test with test values from list T
    T = [10, -10, 'h', [], {}, '', 1.0, None, check_this('16'), '\n']
    G = (test_check_this(test_val) for test_val in T)
    for testable_item in T:
        # run test on that testable_item
        print next(G)

    ## Separate the internal logic from the business logic
    ## can this work as a tool in another module? or in the python iterpreter
