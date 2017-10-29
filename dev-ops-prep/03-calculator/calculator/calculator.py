#! /usr/bin/python -tt

class Calculate(object):
    def add_inputs(self, x, y):
        return x+y



if __name__ == '__main__':
    calc = Calculate()
    result = calc.add_inputs(2, 2)
    print result
