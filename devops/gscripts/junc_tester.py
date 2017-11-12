#! /usr/bin/python -tt

"""test runner"""


def do(x):
    return x

def do_that(x):
    return x

def test(got, expected):
    """Compare what ya got with the truth.
    Tell me straight: was is it everything you expected it be?
    """

    result = ''
    if got == expected:
        result = 'PASS'
    else:
        result = ' X'
    return '{:10s} got: {:15s} expected: {}'.format(result, repr(got), repr(expected))


if __name__ == '__main__':


    # try the map function?

    func1_values = [(do(10), 10),
                    (do(10), 100),
                    (do(99), 99)
                    ]

    func2_values = [(do_that(120), 120),
                    (do_that(14430), 13300),
                    (do_that(9900), 9900)
                    ]

    test_suite = [func1_values,
                func2_values]

    for test_values in test_suite:
        for got, expected in test_values:
            print test(got, expected)


#    for got, expected in func2_values:
#        print test(got, expected)
