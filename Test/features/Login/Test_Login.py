from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Drivers.Chrom_Driver
import pytest
from pathlib import Path
import os
from Utilities import BaseClass

class TestLoginFunctionality(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def test_verify_and_click_login_button(self):
        xpath_login_btn = "//input[@id='login_homepage' and @data-qa-id='home-page-login']"
        try:
            self.driver.find_element(By.XPATH, xpath_login_btn).click()
            print("hi")
        except Exception as e:
            print("bi")
            raise e
