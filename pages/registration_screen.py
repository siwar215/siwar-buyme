import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class Registration(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        wait = WebDriverWait(driver, 3)

    def setUp(self):
        f = open('config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.base_page = BasePage(self.driver)

    def register_success(self):
        self.driver.click_element(By.LINK_TEXT, value="כניסה / הרשמה")

