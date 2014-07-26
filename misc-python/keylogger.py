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



def convert_keylog_text(filename):
	"""create file object from txt file.  Outsource char-removal and word-count to other functions
	"""
	
	f = open(filename, 'r')
	text = f.read()        # create a SINGLE string

	# remove extra chars
	cleanedText = remove_char(text)
	
	

	splitTextListed = split_text(cleanedText)    # returns a list, each element define by newline

	
	#word count
	word_count_d = count_words(splitTextListed)
	
	#print splitTextListed
	#for section in splitText:
	#	print section

	#split cleanedText by new line.  creates a list where eacg eleemtbn is line.



	sys.exit(0)

	# count

	# count top

	# mimic using random sample from a word's NEXT words


def count_words(splitTextListed):
	"""Create a word count from a list of strings
	"""
	l = splitTextListed
	d = {}

	for string in splitTextListed:
		print string






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


def main():
	"""Take command line args.  If filename is not specified,
	then resort to default keylog text file.
	"""

	assignDefault = False
	filename = ''


	# IF no command line args, assing defulat
	# if there are not 2 args from command line, or if 2 arg isn't valid then defualt to keylog text
	if len(sys.argv) != 2:
		print "Using default keylog text"
		assignDefault = True


	if assignDefault == True:
		filename = "/Volumes/SubThree/Dropbox/documents/logKext_keyLogger/out_logFile.txt"

	# if a filename is added in command line, then allow it to overwrite the  default
	else:
		filename = sys.argv[2]


	convert_keylog_text(filename)



if __name__ == "__main__":
	"""If called as script, then run main() as expected.  Else, run as module
	"""

	main()
