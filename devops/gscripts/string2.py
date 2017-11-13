#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    #+++your code here+++
    # 1. return string smaller than 3 chars
    if len(s) < 3:
      return s

    # check for ing and ad ly
    elif s[-3:] == 'ing':
        return s + 'ly'

    else:
        return s + 'ing'


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    """Declare variables for indeces and a new string.
    Assign the string argument to the new string var.
    Find substrings 'not' and 'bad'.
    Save and compare their starting index. Which appears first?
    If subtext conditions are not met:
        Return the new string (equal to s argument):
    If 'bads' starting index is greater than 'nots' starting index,
        Then replace the substring between 'n----------------bads' with 'good'
        Save the concatenated new string into new string variable
    Return the new string
    """
    nots_index = 0
    bads_index = 0
    good_string = s
    for i, char in enumerate(s):
        if s[i:i+3] == 'not':
            nots_index = i
        if s[i:i+3] == 'bad':
            bads_index = i

    if bads_index > nots_index:
        good_string = s[:nots_index] + 'good' + s[bads_index+3:]

    return good_string

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad_again(s):
    """Ooooh, let's use the string.find(char) function!
    That'll make life easier, aye?

    Oooh, the string.find(char) returns the index!!! NICE
    Well, actually, string.find(char) returns the number of occurences

    Welllllll, aaaactually it does return the index

    Oh snap, and returns -1 if the char does not live in the string
    """

    # simultaneous assignemnt. COOL
    not_bad = s.find('not'), s.find('bad')

    # test for existence. if either not or bad do not exist, return orignal string
    if -1 in not_bad:
        return s

    # If 'NOT' appears after 'BAD', let the original string pass
    elif not_bad[0] > not_bad[1]:
        return s

    #else:
        # do this
    return s.replace(s[not_bad[0]:not_bad[1]+3], 'good')




    #if either n n == -1:
    #    return s
    # verify that the two substrings live in the string
    #   AND verify that the starting index for 'bad' is greater than 'not'
    #       if these conditions aren't met, return the original string










# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#a-front + b-front + a-back + b-back
def front_back(a, b):
    """Checks for string with even num chars and returns two halves"""
    # if even split into front and back, save strings
    both = a, b
    l_all = []

    for s in both:
        # lame solution! address the string separately
        if len(s) % 2 == 0:
            l_all.append(s[:len(s)/2])
            l_all.append(s[len(s)/2:])
        else:
            l_all.append(s[:(len(s)/2)+1])
            l_all.append(s[(len(s)/2)+1:])


    #a-front[0] + b-front[2] + a-back[1] + b-back[3]
    return '{}{}{}{}'.format(l_all[0], l_all[2], l_all[1], l_all[3])

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'not_bad_again'
  test(not_bad_again('This movie is not so bad'), 'This movie is good')
  test(not_bad_again('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad_again('This tea is not hot'), 'This tea is not hot')
  test(not_bad_again("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
