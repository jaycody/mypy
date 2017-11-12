#! /usr/bin/python -tt

"""simple function tester"""

def do(x):
    return x

def test(got, expected):
    """Compare what you got with what you expected.
    Report back please
    """

    results = ''
    if got == expected:
        results = '  OK'
    else:
        results = '   X'

    return '{:5s}  got: {:10s} expected: {}'.format(results, repr(got), repr(expected))


if __name__ == '__main__':



    print test(do(10), 10)
    print test(do(10), 9990)
