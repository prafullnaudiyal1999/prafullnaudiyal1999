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

@pytest.fixture(scope="class")
def driver_setup():
    # chrome_driver_path = "C:\LeariningGithub\Drivers\Chrom_Driver\chromedriver.exe"
    # service = Service(chrome_driver_path)
    # driver = webdriver.Chrome(service=service)
    # initilise the webdriver
    global driver
    driver = webdriver.Chrome()
    url = "https://enterprise.monotype.com"
    # Navigate to url
    driver.get(url)
    driver.implicitly_wait(10)
    # explicit wait
    # WebDriverWait(driver, 30).until(EC.url_to_be(url))
    print(f"Welcome to Automation of : {driver.title}")
    yield
    driver.quit()