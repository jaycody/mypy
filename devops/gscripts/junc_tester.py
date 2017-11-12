#! /usr/bin/python -tt

"""test runner"""


def do(x):
    return x

def test(got, expected):
    """Compare what ya got with the truth.
    Tell me straight: was is it everything you expected it be?
    """

    result = ''
    if got == expected:
        result = 'PASS'
    else:
        result = 'X'
    return '{:10s} got: {:15s} expected: {}'.format(result, repr(got), repr(expected))


if __name__ == '__main__':


    print test(do(10), 10)
