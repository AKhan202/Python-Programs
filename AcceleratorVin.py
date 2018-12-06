import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from builtins import dir
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lib2to3.tests.support import driver
import time
# import pandas as pd


class Test(unittest.TestCase):

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

       # vinid_element =
        self.driver.find_elements_by_xpath(
            '//*[@id="MasterPageContents_TabContainer1_TabDetails_ucVehicleInformation_tblDataHeader"]/tbody/tr[2]/th[1]')

      #  vin_data =
        self.driver.find_elements_by_xpath(
            '//*[@id="MasterPageContents_TabContainer1_TabDetails_ucVehicleInformation_tblDataHeader"]/tbody/tr[2]/td[1]')

        data = vin_data.get_attribute('title')

        self.driver.quit()

        print("Health report printed")

    def vehicleData(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
