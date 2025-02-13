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
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Adding a handler to make sure logs are flushed and printed immediately
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logging.getLogger().addHandler(console_handler)


def test_driver_setup():
    # chrome_driver_path = "C:\LeariningGithub\Drivers\Chrom_Driver\chromedriver.exe"
    # service = Service(chrome_driver_path)
    # driver = webdriver.Chrome(service=service)
    # initilise the webdriver
    global driver
    driver = webdriver.Chrome()
    url = "https://enterprise.monotype.com"
    # Log the start of the test
    logging.info(f"Starting automation on: {url}")
    # Navigate to url
    driver.get(url)
    driver.implicitly_wait(10)
    # explicit wait
    # WebDriverWait(driver, 30).until(EC.url_to_be(url))
    logging.info(f"Welcome to Automation of : {driver.title}")
    xpath_login_btn = "//input[@id='login_homepage' and @data-qa-id='home-page-login']"
    xpath_mtf_img = "//img[@id='prompt-logo-center']"
    logging.info("Attempting to click the login button...")
    try:
        driver.find_element(By.XPATH, xpath_login_btn).click()
        logging.info("Login button clicked successfully.")
    except Exception as e:
        logging.error(f"Error occurred while clicking login button: {str(e)}")
        raise e
    logging.info("Attempting to verify the image...")
    try:
        image = driver.find_element(By.XPATH, xpath_mtf_img)
        assert image.get_attribute("src") == "https://d20o8o00kc97oh.cloudfront.net/assets/images/MT-fonts-app-logo.svg"
        assert image.get_attribute("alt") == "Monotype."
        logging.info("Image is loaded correctly with the expected src and alt text.")
    except AssertionError:
        logging.error("Image src or alt text does not match the expected values.")
        raise
    except Exception as e:
        logging.error(f"Error occurred while verifying the image: {str(e)}")
        raise e

    finally:
        # Quit the driver after the test
        logging.info("Quitting the driver.")
        driver.quit()