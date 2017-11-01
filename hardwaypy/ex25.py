# ex25:  Even More Practice			 (file by mk.py)

'''
list.split(' ')  # according to whatever's in the quotes
sorted(list)

DOCUMENTATION COMMENTS - defined by triple double-quotes

Import foo.py as a module foo into another file:
	'import ex25'
		# then use dot syntax to call the function foo.function
	'from ex25 import *'  
		# from foo.py, import all functions
	
HELP from interactive python: (the module must be loaded first)
	help(ex25) 					# see documentation comments for all functions
	help(ex25.break_words)		# see documentation comments for single function
'''


def break_words(stuff):
	"""This function will break up words"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words (Alphabetically by default)."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last words after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and lastwords of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorst the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


