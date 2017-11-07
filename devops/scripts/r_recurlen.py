#! /usr/bin/python -tt

"""Recursively counts the length of a string and returns the answer
"""


def len_recur(string_to_count):
    print '==================================='
    if isinstance(string_to_count, basestring):
        print "\tVerified input:'{}' isinstance of basestring\n".format(string_to_count)
        return 'PASSED'
    else:
        print "\tInput:'{}' is not a basestring.".format(string_to_count)
        print "\tInput:'{}' is {}".format(string_to_count, type(string_to_count))
        return 'FAILED'




def test_len_recur(test_num=1, feed_it_this='default_string'):
    """Various tests for the len_recur function
    """
    print ''
    # test 1: expected successs
    if test_num == 1:
        # test here
        print "\nTest:{} ran with input '{}'".format(test_num, feed_it_this)
        result = len_recur(feed_it_this)
        return result

    # test 2: expected fail. sending non string
    if test_num >= 2:
        # test here
        print "\nTest:{} ran with input '{}'".format(test_num, feed_it_this)
        result = len_recur(feed_it_this)
        return result

    else:
        return "ran 0 tests"

# test 1 : use default test values
#print 'Test:{} result:{}'.format(1, test_len_recur())

# test 2 :
test = 2
send = 'NOT THE DEFAULT',
print '---> Test {}: {} ****'.format(test, test_len_recur(test,send))

test = 3
send = []
print '---> Test {}: {} ****'.format(test, test_len_recur(test,send))
print ''
