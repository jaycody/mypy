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
    #print 'tests:'
    #print test(check_if('sent_to_test_and_w'), 'sent_as_expected')
    #print test(check_if('got_expected'), 'got_expected')

    ##### FORMAT!!  #####
    res = ['Homie McHomeboy', 35,  24.798]  # print this
    args = (10, 5, 2.2)                     # with these dimensions
    print('{0[0]:{1}s} {0[1]:{2}d} {0[2]:{3}f}'.format(res, *args))
    ## where:
    ##  's' # format a STRING with n spaces, left justified by defau
    ##  'd' # format an INT reserving n spaces, right justified by default
    ##  'f' # format a float, reserving n spaces, and .n spaces after the decimal point, right justfied by default.
    ##  AND UNPACK THE *args

if __name__ == '__main__':
    main()
