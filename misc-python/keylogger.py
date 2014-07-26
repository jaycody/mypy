#!/usr/bin/env python -tt

"""jstephens - pyfu - 2014 july
Process the output from my keylogger:
- /Volumes/SubThree/Dropbox/documents/logKext_keyLogger/out_logFile.txt
1. convert to single string
2. remove unnecessary chars

3. Mimic? using mimic module
4. ??
- remove extra chars using the wourdcount2 module's remove_char function
- can mimic the keylogger using the mimic_dict function from mim2 module

usage:

"""

import sys

def convert_file_to_file_object(filename):
	"""Takes a text file and returns a single string
	"""

	# to track the commmand line instructions
	f = open(filename, 'r')
	text = f.read()        # create a SINGLE string


	return text


def convert_keylog_text(filename):
	"""Manage word count process.
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



	#print splitTextListed
	#for section in splitText:
	#	print section

	#split cleanedText by new line.  creates a list where eacg eleemtbn is line.



	sys.exit(0)

	# count

	# count top

	# mimic using random sample from a word's NEXT words


def count_words(splitTextListed):
	"""Count number of words in a list of strings, each string a group of words
	"""
	wordList = []

	d = {}

	# 1. currently words are grouped by newline and listed in splitTextListed
	# 2. for each ground of words, split into a list of words.
	# 3. then iterate through list of words from group and append every item to master list
	for groupedString in splitTextListed:
		# take each group of words and split according to whitespace
		splitGroup = groupedString.split()
		# iterate through each word in the group and append that word to a master list
		for word in splitGroup:
			if word != None:
				wordList.append(word)


	#print wordList

	for word in wordList:
		# first standardize cases
		word = word.lower()
		# look for the word in the dicts keys.  if not there, add it.  if it is, add 1 to value
		if word in d:
			d[word] += 1
		else:
			d[word] = 1

	return d




def split_text(cleanedText):
	"""Split a string by newline.  Return a list containing sections by newline.
	"""



	splitText = cleanedText.split('\n')
	return splitText


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

	listOfSpecialChars = ['<del>', '<esc>', '<cntrl>', '<tab>', '<cmd>', '<right>', '<left>', '<down>', '<up>', '<shift>']

	for item in listOfSpecialChars:
		if item in text:
			text = text.replace(item, '')
			remove_char(text)     # recursively call until item no longer in text, then fail condition
	return text

	"""
	if '<del>' in text:
		text = text.replace('<del>', '')
		remove_char(text)
	if '<esc>' in text:
		text = text.replace('<esc>', '')
		remove_char(text)
	if '<cntrl>' in text:
		text = text.replace('<cntrl>', '')
		remove_char(text)
	if '<tab>' in text:
		text = text.replace('<tab>', '')
		remove_char(text)
	if '<cmd>' in text:
		text = text.replace('<cmd>', '')
		remove_char(text)
	if '<right>' in text:
		text = text.replace('<right>', '')
		remove_char(text)
	if '<left>' in text:
		text = text.replace('<left>', '')
		remove_char(text)
	if '<up>' in text:
		text = text.replace('<up>', '')
		remove_char(text)
	if '<down>' in text:
		text = text.replace('<down>', '')
		remove_char(text)
	if '<shift>' in text:
		text = text.replace('<shift>', '')
		remove_char(text)
	#if '(' in text:
	#	text = text.replace('(', '')
	#	remove_char(text)
	#if ')' in text:
	#	text = text.replace(')', '')
	#	remove_char(text)
	#if '[ ]' in text:
	#	text = text.replace('[ ]', '[]')
	#	remove_char(text)
	return text
	"""

def mimic_style(filename):
	"""Mimic writing style of a text file.
	Take a text file and return a text of same length written with similar style
	Select randomly one word from the list of words that follows every word.
	"""
	print 'made it to mimic_style function'


def main():
	"""Take command line args.  If filename is not specified,
	then resort to default keylog text file.
	"""

	assignDefault = False
	filename = ''


	# IF no command line args, assing defulat
	# if there are not 2 args from command line, or if 2 arg isn't valid then defualt to keylog text
	if len(sys.argv) != 3:
		print "Usage:  ./keylogger.py {--count | --mimic } filename"
		print " ========> Defaults to a count of words in keylogger text"
		assignDefault = True

	if assignDefault == True:
		filename = "/Volumes/SubThree/Dropbox/documents/logKext_keyLogger/out_logFile.txt"
	# if a filename is added in command line, then allow it to overwrite the  default
	else:
		filename = sys.argv[2]

	if sys.argv > 2:
		if sys.argv[1] == '--count':
			convert_keylog_text(filename)
		elif sys.argv[1] == '--mimic':
			mimic_style(filename)
	else:
		convert_keylog_text(filename)

if __name__ == "__main__":
	"""If called as script, then run main() as expected.  Else, run as module
	"""

	main()
