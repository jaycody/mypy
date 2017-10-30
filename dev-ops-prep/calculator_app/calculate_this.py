#! /usr/bin/python -tt

class Calculate(object):
    def add_inputs(self, x, y):
        if (type(x) and type(y)) == int:
            return x+y
        else:
            raise TypeError('Invalid Types. Expected Ints. Got {} and {}'
                            .format(type(x), type(y)))


if __name__ == '__main__': 
    calc = Calculate()
    result = calc.add_inputs(2, 2)
    print result
