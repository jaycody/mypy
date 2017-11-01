#!/usr/bin/env python -tt

""" jstehens - pyfu - selenium unittest collect all links from search results

Conduct search.  
From search results, collect all links.
Create dictionary of links with keys for link attributes ('href', etc)

"""



import unittest
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class TestSearchResults(unittest.TestCase):

	####################
	@classmethod
	def setUpClass(cls):
		cls.searchTerm = raw_input("enter search term: ")

		

	@classmethod
	def tearDownClass(cls):
		print "running tearDown for class"

	#######################
	
	###### TEST CASE SETUP
	def setUp(self):
		self.driver = webdriver.Firefox()
		

	def tearDown(self):
		print "\nrunning tearDown for test case"
		raw_input('enter to continue:')
		self.driver.close()
	######################
	

	def test_google_exists(self):
		"""Is this google homepage?  Check that page title = Google"""
		self.driver.get("http://www.google.com")
		self.assertIn("Google", self.driver.title)

	def test_search_results(self):
		"""Do search results contain the search term?
		Check that the search term appears in the top 5 search results
		"""
		self.driver.get("http://www.google.com")
		searchbox = self.driver.find_element_by_name('q')
		searchbox.send_keys(self.searchTerm)
		searchbox.send_keys(Keys.RETURN)
		raw_input('\nenter to continue:')
		# Get a list of all search results
		searchResultsList = self.driver.find_elements_by_tag_name('a')
		print "\nsearch results list data type = ", type(searchResultsList)
		print "--> len of search results list = ", len(searchResultsList)
		print "--> search term = '%s'" % self.searchTerm

		## Find first 10 results appearing after 1st instance of search term
		#indexTermAppears = self.getIndexOfFirstAppearance(searchResultsList)
		#print "index Term Appears data type = ", type(indexTermAppears)




		#firstTen = searchResultsList[indexTermAppears:indexTermAppears+10]
		
		# Look for the search term in each href of all 10 search results
		firstTen = searchResultsList
		if len(firstTen) == 0:
			self.fail("Test failed b/c no links were found")
		failCount = 0
		passCount = 0
		listhrefs = []

		for link in firstTen:
			linkName = link.get_attribute('href')
			print "linkName type: ", type(linkName)
			# type check does NOT require quotes for the answer
			if type(linkName) == unicode: ##########################
				listhrefs.append(linkName)
				print "linkName: ", linkName, "  -- linkName type = ", type(linkName)
				if self.searchTerm not in linkName:
					failCount += 1
					print "search term: '%s' does NOT appear in %s " % (self.searchTerm, linkName)
				else:
					passCount += 1
					print "\nsearch term: '%s' DOES appear in %s " % (self.searchTerm, linkName)
				
		print "\npassCount = %d   ---------   failCount = %d" % (passCount, failCount)
		
		# creat a list of the top 20
		searchTermList = []
		maxLinks = 20
		currentLinks = 0
		isTriggered = False
		numLinksMissingSearchTerm = 0
		numLinksContainingSearchTerm = 0

		for href in listhrefs:
			if not isTriggered:
				if 'automation' in href:
					isTriggered = True
					currentLinks += 1 
					searchTermList.append(href)
			elif currentLinks < maxLinks:
				searchTermList.append(href)
				currentLinks += 1

		print "search term list contains the 20 links after first instance of search term"
		print searchTermList

		for link in searchTermList:
			if 'automation' in link:
				numLinksContainingSearchTerm += 1
			else:
				numLinksMissingSearchTerm += 1
				print "search term: ", self.searchTerm, "does NOT appear in \n  - link: ", link

		raw_input('enter to continue')

		# Is Fail Count sitll zero?

		self.assertEqual(numLinksMissingSearchTerm, 0)




	def getIndexOfFirstAppearance(self, searchResultsList):
		"""Find and Return the first 10 search results which immediately follow
		the first instance of the search term appearing in the search results.
		"""

		indexTermAppears = 0
		#firstTen = []
		lenResultsList = len(searchResultsList)

		for index in range(lenResultsList):
			link = searchResultsList[index]
			linkName = link.get_attribute('href')
			if type(linkName) == 'unicode':
				if self.searchTerm in linkName:
					indexTermAppears = index
					return indexTermAppears
				else:
					print "self.searchTerm: '%s' is NOT in searchResultsList" % self.searchTerm
					return 0








if __name__ == '__main__':

	unittest.main()

