#!/usr/bin/env python -tt

"""jstephens - pyfu - 2014 july
Either counts the words or mimics the writting style from the keylogger text
"""

import sys
import random


def convert_keylog_text(filename):
	"""Manage word count process.  From file, print word count to console.
	- Outsource file conversion
	- Outsource char-removal and word-count to other functions
	- Outsource text splitting 
	- Outsource word counting
	"""

    # convert text file into string of words
	text = convert_file_to_file_object(filename)


	# remove extra chars
	cleanedText = remove_char(text)
	

	splitTextListed = split_text(cleanedText)    # returns a list, each element define by newline


	# count the words in a list of strings --- send a list of strings 
	word_count_d = count_words(splitTextListed)

	# iterate through the key/value pairs sorted by value.  print the resulting tuple
	d = word_count_d
	for k in sorted(d.keys(), key=d.get):
		if d[k] > 100:
			print k, d[k]
		#print "%s  =>  %s" % (pair)

	sys.exit(0)

def convert_file_to_file_object(filename):
	"""Takes a text file and returns a single string
	"""

	# to track the commmand line instructions
	f = open(filename, 'r')
	text = f.read()        # create a SINGLE string


	return text

def remove_char(stringedText):
	""" Scrub string of unnecessary chars.  Return a new clean string
	Method:
	- remove (<del>, <esc>, <cntrl>, <tab>, <cmd>, <right>, <left>, <down>, <up>)
	- Recursively??
	- Get length of
	- won't work for entire file, need to chop into indicividual words.
	"""
	text = stringedText
	#cleanedText = ''      # need a place to store the chars that actually belong
	
	# new method that skips all the if statement branches
	# 1. Put all the special chars in a single list
	# 2. Iterate through the list when analyzing each char
	# 3. recurs as before

	# if it's Alice.txt, then use the full list.  otherwise use shorter list
	if sys.argv[2] == '-2':
		listOfSpecialChars = [',', '.', '?', '!', '`', '<del>', '<esc>', '<cntrl>', '<tab>', '<cmd>', '<right>', '<left>', '<down>', '<up>', '<shift>']
	else:
		listOfSpecialChars = ['<del>', '<esc>', '<cntrl>', '<tab>', '<cmd>', '<right>', '<left>', '<down>', '<up>', '<shift>']


	for item in listOfSpecialChars:
		if item in text:
			text = text.replace(item, '')
			remove_char(text)     # recursively call until item no longer in text, then fail condition
	return text

def split_text(cleanedText):
	"""Split a string by newline.  Return a list of words.
	"""

	wordList = []

	splitTextListed = cleanedText.split('\n')
	

	for groupedString in splitTextListed:
		# take each group of words and split according to whitespace
		splitGroup = groupedString.split()
		# iterate through each word in the group and append that word to a master list
		for word in splitGroup:
			if word != None:
				wordList.append(word)

	return wordList

def count_words(wordList):
	"""Count number of words in a list of strings.  Return dict with word = count
	"""

	d = {}

	for word in wordList:
		# first standardize cases
		word = word.lower()
		# look for the word in the dicts keys.  if not there, add it.  if it is, add 1 to value
		if word in d:
			d[word] += 1
		else:
			d[word] = 1

	return d

def create_mimic_dict(wordList):
	"""Create and return a dict listing all words that follow each key word from a string
	"""
	d = {}
	prev = ''
	
	for word in wordList:
		if not prev in d:
			d[prev] = [word]
		else:
			d[prev].append(word) 
		prev = word

	return d

def print_mimic_wordlists(mimic_dict):
	"""Print popular words followed by a list of all the words which follow that popular word.
	Define popular as any word used more than 10 times.
	"""

	for key in mimic_dict.keys():
		# If the word is used more than 10x, then it should have more than 10 words in it's mimic list.
		if len(mimic_dict[key]) > 10:

			print "===== '%s' ====> followed by" % key
			for item in mimic_dict[key]:
				print item, "",
			print "\n"

def create_mimic_text(mimic_dict):
	"""Create a new text that mimics the style of the original text.
	"""
	#f = open('mimic_text.txt', 'r+')
	f = open("/Volumes/SubThree/Dropbox/documents/logKext_keyLogger/out_logFile_mimicked.txt", "r+")

	s = ''
	
	for keyword in mimic_dict.keys():
		randNext = random.choice(mimic_dict[keyword])
		print keyword, randNext,
		s = " " + keyword + " " + randNext
		#f.writelines(keyword)
		#qf.writelines(randNext)
		f.writelines(s)
		#s = str(s + keyword + randNext),
	f.seek(0)

	f.close()

def mimic_style(filename):
	"""Mimic writing style of a text file.
	Take a text file and return a text of same length written with similar style
	Select randomly one word from the list of words that follows every word.
	"""
	#print 'made it to mimic_style function'

	# Convert file to single string
	singleStringOfText = convert_file_to_file_object(filename)

	# Clean the text
	cleanedString = remove_char(singleStringOfText)

	wordList = split_text(cleanedString)

	#print wordList
	mimic_dict = create_mimic_dict(wordList)

	# ask for user input.  If print dict or if mimic text?
	ans = raw_input('print mimicked words? y/n: ')
	if ans == 'y':
		# print the mimmicked words:
		print_mimic_wordlists(mimic_dict)

	ans = raw_input('create mimicked text? y/n: ')
	if ans == 'y':
		create_mimic_text(mimic_dict)
	else:
		sys.exit(0)
	

	sys.exit(0)
	#cleanedText = remove_char()

def main():
	"""Take command line args.  If filename is not specified,
	then resort to default keylog text file.
	"""

	# IF no command line args, assing defulat
	# if there are not 2 args from command line, or if 2 arg isn't valid then defualt to keylog text
	filename = ''
	usage = "Usage:  ./keylogger.py {--count | --mimic } { -1 = keylog text  | -2 = alice in wonderland }"
	if len(sys.argv) != 3:
		print usage
		sys.exit(1)

	option = sys.argv[1]
	fileOption = sys.argv[2]

	if fileOption == '-1':
		filename = "/Volumes/SubThree/Dropbox/documents/logKext_keyLogger/out_logFile.txt"
	elif fileOption == '-2':
		filename = "/jayjaycody/mypy/google-py/basic/alice.txt"	
	else:
		print "unknown fileOption" + fileOption
		print usage
		sys.exit(1)


	if option == "--count":
		print "Counting words from file: \n  " + filename
		convert_keylog_text(filename)
	elif option == "--mimic":
		print "mimicking text from file: \n  " + filename
		mimic_style(filename)
	else:
		print "unknown option: " + option
		sys.exit(1)

if __name__ == "__main__":
	"""If called as script, then run main() as expected.  Else, run as module
	"""

	main()
