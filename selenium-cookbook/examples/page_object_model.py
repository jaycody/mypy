#!/usr/bin/env python -tt

""" jstephens - pyfu - unittest, selenium, page object model

Implement Page Object Model:
- Page class:  A Base class from which all subsequent Page Objects can inherit common behaviors
- LoginPage class:  Model the behavior of the login page
- test_login:  assert successful login
- main

What can the Page base class do?
- Initial opening of a website and check that it's on the page it's intending to be on
- find and elment for you
- open a url via interface open(self)
- on_page() ? are we on the page we're supposed to be on
- script() execut a script
- send_keys

What behavior is modeled by the LoginPage class?
ans:  The Page Object says:  
1. 'There is such a thing as a login page at test.axial.net.
2. Here are the locations of 3 import elements on the login page:
     1. email field
     2. password field
     3. submit button
3. On the login page, we'll want to perform a few simple actions, listed here:
     1. open the login page
     2. type email in the email field
     3. type password in the password field
     4. submit the password and email after entering them

Now let's run a test!
1. From within the test, pass the active driver page to the LoginPage class
       - this creates an instance of the Page Object class called login_page
       - We know this instance of the LoginPage class is actually the login page
           (and not, say, the Contacts page) because the active selenium driver window
           was on the login page when the driver was passed to the LoginClass
2. Now we have a driver window displaying the login page 
       and we have an object called login_page that represents what's in the driver window 
3. Now treat the object as if you already know everything about it.
		- You won't find any 'find_element_by' here.  
       	- So on your page instance, call your own tools
       	  login_page.open()
       	  login_page.type_email(username)
       	  login_page.type_password(password)
       	  login_page.submit()
           
          and asseert that our new location is NOT the still the login page
              asset not login_page.on_page()  
                 # here the object calls on its on_page feature from the base class

Thanks to Steve from Axial Market for the example:
https://gist.github.com/axialmarketsteve/5919625

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
 
class Page(object):
    """
    Base class that all page models can inherit from
    """
 
    def __init__(self, selenium_driver, base_url='https://test.axial.net', parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}
 
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url
 
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
 
    def open(self):
        self._open(self.url)
 
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)
 
    def script(self, src):
        return self.driver.execute_script(src)
 
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print '%s page does not have "%s" locator' % (self, loc)
 
 
class LoginPage(Page):
    """
    Model the login page.
    """
    url = '/login/'
 
    # Locators
    _email_loc = (By.ID, 'id_email')
    _password_loc = (By.ID, 'id_password')
    _submit_loc = (By.CSS_SELECTOR, '#sign_in_bttn')
 
    # Actions
    def open(self):
        self._open(self.url)
 
    def type_email(self, email):
        self.find_element(*self._email_loc).send_keys(email)
 
    def type_password(self, password):
        self.find_element(*self._password_loc).send_keys(password)
 
    def submit(self):
        self.find_element(*self._submit_loc).click()
 
 
def test_that_user_can_login(driver, username, password):
    """
    Test that the user identified by the given credentials can login
    """
    login_page = LoginPage(driver)
 
    login_page.open()
    login_page.type_email(username)
    login_page.type_password(password)
    login_page.submit()
 
    # Make sure we got past the login page
    assert not login_page.on_page(), "Couldn't get past the login page"
 
 
def main():
    try:
        # Selenium 
        driver = webdriver.Firefox()
        username = 'scuba.steve@axial.net'
        password = 'wouldntyouliketoknow'
        test_that_user_can_login(driver, username, password)
    finally:
        # Close the browser window
        driver.close()
 
if __name__ == '__main__':
    main()