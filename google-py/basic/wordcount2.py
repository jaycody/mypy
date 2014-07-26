#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""jstephens - pyfu - 2014 july
test file:  Volumes/SubThree/Dropbox/documents/logKext_keyLogger/out_logFile.txt

Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

#### LAB(begin solution)


def print_words(filename):
  """Prints one per line '<word> <count>' sorted by word for the given file.
  >>> print_words('generic test')
  generic doctest for print_words function.  Arg passed = generic test
  """
  print "generic test for print_words function.  Arg passed = %s" % (filename)

  d = {}
  allLines = []
  allWords = []
  listOfElements = []
  listOfWords = []
  listToRemoveChar = []
  listOfEachLinesElements = []

  ## --DEBUG
  #f = open(filename, 'r')
  #for line in f:
  #  print line,
  
  f = open(filename, 'r')
  for line in f:   #where line = str
    line = line.strip()
    line = line.lower()
    listOfEachLinesElements.append(line.split())
    #print line
  for allWordsInEachLine in listOfEachLinesElements:  # where allWordsInEachLine is a list
    #print eachWordsInEachLine
    for eachWordInEachLine in allWordsInEachLine:     # where eachWordInEachLine is a string
      #print eachWordInEachLine
      #print 'type of eachWordInEachLine = ', type(eachWordInEachLine)
      
      if eachWordInEachLine in d.keys():
        d[eachWordInEachLine] += 1
      else:
        d[eachWordInEachLine] = 1
  
  for key in sorted(d.keys(), key=d.get):
    print key, " ", d[key]



      #allWords.append(eachWordsInEachLine)
  #print allWords

  '''
  f = open(filename, 'r')
  for line in f:   # where line type is string
    print line
    allLines.append(line)
    print "line type = ", type(line)
    #if 'c' in line:
    for letters in line:
      print letters
      allWords.append(letters)
  #print allWords 

  #for eachLine in allLines:
  #  listOfElements.append(eachLine.split())
  #print listOfElements

  print "length of listOfElements = ", len(listOfElements)
  print "length of allWords = ", len(allWords)
  '''


  '''
  for item in listOfElements:
    # remove extra chars
    #print "item type = ", type(item)
    for element in item:
      element = element.lower()
      listOfWords.append(element)

  # Populate Dictionary
  for word in listOfWords:
    if word in d:
      d[word] += 1
    else:
      d[word] = 1
  '''
  #print sorted(d.values())

  #for pair in sorted(d.items(), key=d.get):
  #  print pair[0], '= ', pair[1]
  '''
  listOfChars = []
  dOfChars = {}
  for itemString in d.keys():
    #print "item type is ", type(item)
    for charElement in itemString:
      #print charElement,
      listOfChars.append(charElement)
  print listOfChars
  '''



  ########## SORT DICT BY VALUE #################
  #for key in sorted(d.keys(), reverse=True, key=d.get):
  #  print key, '= ', d[key]
  ###############################################


  sys.exit(0)


def print_top(filename):
  """Prints the top count listing for the given file."""
  #print "print_top function reached"
  
  listOfAllLines = []
  listOfAllWords = []
  topTwenty = []
  d = {}

  f = open(filename, 'r')
  for line in f:
    line = line.strip()
    line = line.lower()
    splitLine = line.split()
    for word in splitLine:
      word = remove_char(word)
      if word != None:
        listOfAllWords.append(word)
  #print listOfAllWords

  for word in listOfAllWords:
    if word in d.keys():
      d[word] += 1
    else:
      d[word] = 1

  for k in sorted(d.keys(), key=d.get, reverse=True):
    topTwenty.append(k)

    #print k, d[k]

  print topTwenty[:20]

  print "Top 20 words used 'Alice in Wonderland, "
  for i in range(20):
    print topTwenty[i], "= ", d[topTwenty[i]]


def remove_char(word):
  """Remove all non-letter chars from each string and return the results.
  Recursively calls itself until base case reached.
  """
  newWord = ""
  if word == None:
    return
  elif '(' in word:
    newWord = word.replace('(', '')  # replace open paran with no space
    remove_char(newWord)
  elif ')' in word:
    newWord = word.replace(')', '')  # replace open paran with no space
    remove_char(newWord)
  elif "'" in word:
    newWord = word.replace("'", "")  # replace open paran with no space
    remove_char(newWord)
  elif "," in word:
    newWord = word.replace(",", "")  # replace open paran with no space
    remove_char(newWord)
  elif "." in word:
    newWord = word.replace(".", "")  # replace open paran with no space
    remove_char(newWord)
  elif "!" in word:
    newWord = word.replace("!", "")  # replace open paran with no space
    remove_char(newWord)
  elif "`" in word:
    newWord = word.replace("`", "")
    remove_char(newWord)
  elif "?" in word:
    newWord = word.replace("?", "")  # replace open paran with no space
    remove_char(newWord)
  elif ":" in word:
    newWord = word.replace(":", "")  # replace open paran with no space
    remove_char(newWord)
  elif ";" in word:
    newWord = word.replace(";", "")  # replace open paran with no space
    remove_char(newWord)

  else:
    return word



def word_count_dict(filename):
  """Returns a word/count dict for this filename."""
 


def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""

 

##### LAB(end solution)


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
