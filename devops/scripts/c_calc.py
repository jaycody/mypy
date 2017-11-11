#! /usr/bin/python -tt

"""Adds 2 ints and returns the sum

also raises a TypeError when inputs are other than ints
"""


class Calculate(object):

    def add_inputs(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return x+y
        else:
            #raise TypeError
            return type(x), type(y), 'Invalid Types. Expected ints. Got {} and {}'.format(type(x), type(y))


if __name__ == '__main__':
    calc = Calculate()

    print '\n1st try:'
    result = calc.add_inputs(2, 'h')
    print result


    print '\n2nd try:'
    result = calc.add_inputs(2, 2)
    print result
