#! /usr/bin/env python -tt
""" contains a doctest for all functions

- run doctest as follows:

$ python -m doctest -v string2.py

"""
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
  """Determine if a string is less than 3 characters.
  If it is, then return the string unchanged.
  If not, then add 'ing' to the end.
  Unless the string already has 'ing', in which case, just ad 'ly'.
  >>> verbing('jack')
  'jacking'
  >>> verbing('it')
  'it'
  >>> verbing('coding')
  'codingly'
  """
  
  if len(s) < 3: 
    return s
  elif s[-3:] == 'ing':
    newly = s + 'ly'
    return newly
  else:
    newing = s + 'ing'
    return newing



# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  """Replace 'not...bad' with 'good' and return the results
  >>> not_bad('this pasta is delicious')
  'this pasta is delicious'
  >>> not_bad('this pasta is not that bad')
  'this pasta is good'
  >>> not_bad('this pasta is not for eating')
  'this pasta is not for eating'
  """
  if 'not' in s:
    notIndex = s.index('not')
    if 'bad' in s:
      badIndex = s.index('bad')
      if badIndex > notIndex:
        # everyting up to not = s[:notIndex]
        # everything beyond 'bad' = s[badIndex+3:]
        newString = s[:notIndex] + "good" + s[badIndex+3:]
        return newString
      else:
        return s
    else:
      return s
  else:
    return s


  # +++your code here+++
  


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  """Divide two strings and stitch together such that front halves a and b  precede back halves.
  Place modulo of divided string with odd number of chars to first half.
  >>> front_back('four', 'tool')
  'fotourol'
  >>> front_back('twitter', 'objects')
  'twitobjetercts'
  """
  firstA = ""
  secondA = ""
  firstB = ""
  secondB = ""
  midWayIndex = 0
  midWayIndexB = 0
  lenA = len(a)
  lenB = len(b)

  if lenA % 2 == 0:  #then no remainder
    midWayIndex = lenA/2
    firstA = a[:midWayIndex]
    secondA = a[midWayIndex:]
  else:
    midWayIndex = (lenA/2)+1
    firstA = a[:midWayIndex]
    secondA = a[midWayIndex:]

  if lenB % 2 == 0:
    midWayIndexB = len(b)/2
    firstB = b[:midWayIndexB]
    secondB = b[midWayIndexB:]
  else:
    midWayIndexB = (len(b)/2)+1
    firstB = b[:midWayIndexB]
    secondB = b[midWayIndexB:]

  
  return firstA + firstB + secondA + secondB


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
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
