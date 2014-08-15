#!/usr/bin/env python -tt

""" jstephens - pyfu - selenium unittest google homepage test


Script that tests google search results using Selenium Webdriver and Python unittest
"""



import unittest
from selenium import webdriver



class TestGooglePage(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://google.com")


	def test_google_exists(self):
		self.assertIn("Google", self.driver.title)

	def tearDown(self):
		self.driver.close()


if __name__ == '__main__':

	unittest.main()
