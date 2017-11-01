#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
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

from wordcount2 import remove_char


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it.
  Take file into a single giant string and then split on whitespace.
  For each word, show each word that normally appears after that word
  """
  d = {}
  cleanedWords = []
  listOfValues = []

  f = open(filename, 'r')
  fileStr = f.read()
  #print fileStr
  listOfElements = fileStr.split()
  for word in listOfElements:
    word = remove_char(word)
    if word != None:
      cleanedWords.append(word.lower())
  #print cleanedWords
  
  for word in cleanedWords:
    wordIndex = cleanedWords.index(word)
    nextWord = cleanedWords[wordIndex+1]
    nextWordIndex = cleanedWords.index(word)+1
    
    #print "word = %s, wordIndex = %d, nextWord = %s, nextWordIndex = %d" % (word, wordIndex, nextWord, nextWordIndex)

    # if the word exists in the dict
    if word in d.keys():
      #print word, " <==this then next word ==>", d[word]
      # but the word hasn't yet been added to the key's list of words, then add the word
      listOfValues = d[word]
      print listOfValues
      print d.keys()
      if not nextWord in listOfValues:

        print "nextWord %s is NOT in d[word]" % nextWord
        d[word].append(nextWord)
    # if the word is not already in dict, then create a key 
    #whose value is a list populated with next wordIndex
    else:
      d[word] = [cleanedWords[wordIndex+1]] 

  #for k in sorted(d.keys()):
  #  print k, "= ", d[k]
  return d


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
