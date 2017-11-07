#! /usr/bin/python -tt

""" Calculates and returns the length of an input string.
Validates data type first.
"""


def fast_string_length(s):
    """Counts and returns the elements in a string.
    Walks throught the string with a for in each iteratior
    """

    count = 0
    for i in s:
        count += 1

    return count


test_string = "blammmmooooh"
print "\nTest_string: '" + test_string + "' has element count of ", fast_string_length(test_string)

test_string = "ba;alsdjga;jga;jga;jgajgajgdjrj"
print "\nTest_string: '" + test_string + "' has element count of ", fast_string_length(test_string)
print 'Verified length: ', len(test_string)
