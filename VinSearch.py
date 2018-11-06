
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from builtins import dir
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lib2to3.tests.support import driver
import time


class Vintest(unittest.TestCase):

    def vinName(self):

        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get(
            "https://evaluet.internationaldelivers.com/service/service_info/Welcome.aspx")

        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(40)
        self.driver.find_element_by_id("txtChassis").send_keys("FH035330")

        self.driver.implicitly_wait(20)

        self.driver.find_element_by_id("btnChassiView").click()

        self.driver.implicitly_wait(30)

        self.driver.find_element_by_id(
            "__tab_MasterPageContents_TabContainer1_TabDetails").click()

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
