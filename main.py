import locators
import data
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTemu:

    driver = None

    @classmethod
    def test_purchase_flow(self):
        # add the driver
        self.driver.get(data.temu_url)