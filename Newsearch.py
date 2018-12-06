'''
Created on Oct 29, 2018

@author: u01n233
'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from builtins import dir
import unittest


class OpenBrowser(unittest.TestCase):

    def setUp(self):

        chrome_path = "C:\\Users\\u01n233\\eclipse-workspace\\NewPythonProjects\\chromedriver\\chromedriver.exe"

        self.driver = webdriver.Chrome(chrome_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com/")
        self.driver.quit()

    def searchVin(self):
        driver = self.driver
        self.searchVin = self.driver.find_element_by_name("vin")
        self.searchVin.send_keys("fh035330")
        self.searchVin.submit()

        self.browser.close()
        self.browser.quit()

        self.assert_("No result found")


if __name__ == '__main__':
    unittest.main()
