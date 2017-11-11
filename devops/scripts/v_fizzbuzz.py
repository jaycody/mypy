#! /usr/bin/python -tt

"""Prints fizzbuzz to console based on modulo"""



def fizzbuzz(x):
    """Print fizz or buzz or fizzbuzz as needed"""

    # print fizz and buzz if modulo 5 & 3 both return 0
    # NICE, this check range thing actually worked!!!
    if x % 3 == 0 == x % 5:
        return 'fizzbuzz!  when x={}'.format(x)

    #Print fizz when val module 3 = 0
    elif x % 3 == 0:
        return 'fizz'

    #Print fizz when val module 3 = 0
    elif x % 5 == 0:
        return 'buzz'

    else:
        return None



def test_fizzbuzz(x=15):
    """Test the fizzbuzzness"""

    ## Test if module 3 remainder 0 prints fizz
    print fizzbuzz(3)

    ## Test if module 5 == 0 print buzz
    print fizzbuzz(5)

    ## test if modulo 5 and 3 = 0 prints fizzbuzz
    print fizzbuzz(15)

    #okay, lets check the full range
    for i in xrange(x):
        if fizzbuzz(i) is not None:
            print fizzbuzz(i)

# test default value
test_fizzbuzz()

# test big num
test_this = 99999999999
test_fizzbuzz(test_this)
