#! /usr/bin/python -tt

"""Converts base 10 positive ints into binary
"""


def convert_to_binary(x):
    """Convert to binary any positive int x of base 10.

    x: positve int
    steps:
    0. convert decimal into base 10 representation
        eg 40932 = 4 * 10**4 + 0 * 10**3 + 9 * 10**2 + 3 * 10**1 + 2 * 10**0
    1. check x % 2 for initial binary digit
    2. Right shift x by dividing by 2
    3. check new x % 2 for next binary digit
    4. repeat until len x == 0
    5. return binary digit
    """
    return x



def test_convert_to_binary():
    """validate the convert_to_binary function

    test for expected success
    test for various failures
    """

    # test 1: do you exist?
    t1 = 4
    return "If you exist, return {} ---> {} returned".format(t1, convert_to_binary(t1))


if __name__ == '__main__':
    print test_convert_to_binary()







#print convert_to_binary('10')
