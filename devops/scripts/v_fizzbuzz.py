#! /usr/bin/python -tt

"""Prints fizzbuzz to console based on modulo"""



def fizzbuzz(x):

    # print fizz and buzz if modulo 5 & 3 both return 0
    # NICE, this check range thing actually worked!!!
    if x % 3 == x % 5:
        return 'fizzbuzz'

    #Print fizz when val module 3 = 0
    if x % 3 == 0:
        return 'fizz'

    #Print fizz when val module 3 = 0
    if x % 5 == 0:
        return 'buzz'




def test_fizzbuzz():
    """Test the fizzbuzzness"""

    ## Test if module 3 remainder 0 prints fizz
    print fizzbuzz(3)

    ## Test if module 5 == 0 print buzz
    print fizzbuzz(5)

    ## test if modulo 5 and 3 = 0 prints fizzbuzz
    print fizzbuzz(15)




test_fizzbuzz()

#print fizzbuzz.func_name
