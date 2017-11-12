#! /usr/bin/python -tt

"""Function tester - simplest version"""


def check_if(x=None):
    return x


def test(got=None, expected=None):
    """Compares the actual against the expected and prints test results.

    got: results from function under test
    expected: known good
    """

    flag = ''
    if got == expected:
        flag = ' OK'
    else:
        flag = '  X'

    results  = "{:5s} got: {:22s} expected: {}".format(flag, repr(got), repr(expected))

    return results





def main():
    #print check_if('to check'),
    print 'tests:'
    print test(check_if('sent_to_test_and_w'), 'sent_as_expected')
    print test(check_if('got_expected'), 'got_expected')

if __name__ == '__main__':
    main()
