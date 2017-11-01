#!/usr/bin/env python -tt

""" jstephens - pyfu - unittest selenium and error handling

Test Case that gets the weather in New York from weather.com

Utility functions:
- is element present?
- collect and iterate through alert messages

Thanks to Steve from Axial Market for the example:
https://gist.github.com/axialmarketsteve/5961128
"""


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
 
class Weather(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.weather.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
 
    def test_weather(self):
        driver = self.driver
        #driver.get(self.base_url + "/")
        driver.get(self.base_url)
        driver.find_element_by_id("typeaheadBox").clear()
        driver.find_element_by_id("typeaheadBox").send_keys("New York, New York")
        driver.find_element_by_css_selector("div.wx-searchButton").click()
        # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Forecast for Today[\s\S]*$")
 
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
 
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
 
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
 
if __name__ == "__main__":
    unittest.main()