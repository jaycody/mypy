#!/usr/bin/env python -tt

""" jstephens - pyfu - unittest selenium via PageObjectModel abstraction

Reduce duplication - Add abstraction - Hide inner implementation
"""


import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPageOjbectModel(unittest.TestCase):

	def setUp(self):
		"""Inititate test function setup"""

	def tearDown(self):
		"""Initiate test function tearDown"""
		print "test function tear down"


	def test_unknown(self):
		"""Test Pagoe Object Model functionality"""






if __name__ == '__main__':

	unittest.main()






