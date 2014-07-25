#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""j stephens - pyfu - 2014 july

topics:
random.choice(list)

Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  
  mimic_d = {}

  f = open(filename, 'r')
  text = f.read()
  text.strip()
  words = text.split()
  prev = ''

  for word in words:
    if not prev in mimic_d:
      mimic_d[prev] = [word]
    else:
      mimic_d[prev].append(word)
    
    prev = word
  
  return mimic_d


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words.
  1. Find given word as key in dict
  2. Return randomly one of the words from the key's list of words
  3. Use that randomly returned words as the next word.
  4. repeat for 200 words
  extra: Feed this program to itself.  
         Include line breaks at about 70 columns

  """
  #print "made it to print_mimic(function)"
  d = mimic_dict

  randNext = ''

  count = 0
  newlineAt = 70
  countColums = 0


  for word in d.keys():
    if count < 20000:
      randNext = random.choice(d[word])
      #print "word = %s, randNext = %s" % (word, randNext)
      if countColums < newlineAt:
        print word, randNext,
        countColums += (len(word) + len(randNext))
      else:
        print ""
        countColums = 0
        newLine = random.randrange(40, 70)

    count += 1

  sys.exit(0)
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  """process the command line input"""

  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
