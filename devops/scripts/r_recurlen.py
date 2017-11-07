#! /usr/bin/python -tt

"""Recursively counts the length of a string and returns the answer
"""


def len_recur(string_to_count):
    """Well, putting the test results print statements in the central function
    is probably a no no. I got a bit carried away, like I was full throttle
    doing brodies in a infinitely large cornfield.
    """

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
    if test_num <= 1:
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

def test_run(test=0, send='default_string_from_runner'):
    """Calls the test function and passes in the args to test.
    test: the specific test case to run in the test_len_recur test suite
    send: the input to pass to the recur function for counting
    """

    result = test_len_recur(test,send)
    print '---> Test {}: {} ****'.format(test, result)
    print ''
    return result

# test default values
test_run()
test_run(1)

############################
##### NOW YOU GETTING FANCY
test = [2,3,4,5,6,7,8]
send = ["not the defaults", [], 'this is from tuple', ('t',), {}, 'test 7 passes right', 'this is 8th test']
failcount = 0
for i in xrange(len(test)):
    result = test_run(test[i], send[i])

    # count the fails
    if result.startswith('F'):
        failcount +=1
    else:
        failcount +=0

print "\n******* FAILCOUNT= {} of {} total tests **********".format(
                                                    failcount, len(test))
