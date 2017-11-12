#! /usr/bin/python -tt

"""test runner

test_suite: list of test cases for each function
test case: 2-value-tuple with 1) string for function name and 2) a list of test_values
test_values: a list of got,expected value pairs saved as tuples

"""


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
    return '  {:10s} got: {:15s} expected: {}'.format(result, repr(got), repr(expected))

def test_runner(full_test_suite):
    """Extract and run each test case from the full test suite"""

    for f_test in full_test_suite:
        print '\nTesting: {}'.format(f_test[0])
        for got, expected in f_test[1]:
            print test(got, expected)

if __name__ == '__main__':

    full_test_suite = []
    ##############################
    ## f1 test info
    f1_name = 'do()'
    f1_values = [(do(10), 10),
                    (do(10), 100),
                    (do(99), 99)
                    ]
    f1 = (f1_name, f1_values)
    ## append f1's test info to the test_suite
    full_test_suite.append(f1)
    ##############################

    ##############################
    ## f2 test info
    f2_name = 'do_that()'
    f2_values = [(do_that(120), 120),
                    (do_that(14430), 13300),
                    (do_that(9900), 9900)
                    ]
    f2 = (f2_name, f2_values)
    ## append f2 test info to the test suite
    full_test_suite.append(f2)
    ##############################

    ##############################
    ## run that thing
    test_runner(full_test_suite)
