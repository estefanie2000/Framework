from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

BASE_URL = "https://www.saucedemo.com/"


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        self.find(by, value).send_keys(text)
