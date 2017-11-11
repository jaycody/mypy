#! /usr/bin/python -tt

""" Guardian of the function threshold"""

def check_this(x):
    """Returns None if value is anything other than a positive int"""

    if not isinstance(x, int):
        return None, x

    if x < 0:
        return None, -1

    return 'PASS', 'input: {} is a positive integer'.format(x)


def test_check_this(val_to_check):
    """Compares check_this function's results with expected"""

    print '\nChecking input: {} ----->'.format(val_to_check)

    results = check_this(val_to_check)

    ## if PASS
    if results[0] is not None:
        return results

    ## if negative
    elif results[1] == -1:
        return '\tNope! {} is as negative as Julian in Less Than Zero'.format(val_to_check)


    ## if NOT INT
    else:
        return '\tNope! Input: {} is of type: {}'.format(val_to_check, type(val_to_check))




if __name__ == '__main__':

    print test_check_this(10)
    print test_check_this(-10)
    print test_check_this('h')
