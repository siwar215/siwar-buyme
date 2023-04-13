import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Constants:
    # login_register = By.LINK_TEXT, "כניסה / הרשמה"
    login_register = By.CLASS_NAME, "notSigned"
    register = By.CSS_SELECTOR, "h1[class=bm-h1]"
    register_type = By.TAG_NAME
    register_value = 'span'
    register_title = By.CLASS_NAME, "lightbox-head"


class Registration(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def setUp(self):
        f = open('config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.base_page = BasePage(self.driver)

    def click_on_login_button(self):
        BasePage.wait_and_click_on_element(self, Constants.login_register)

    def click_on_register(self):
        BasePage.wait_and_click_on_element(self, Constants.register)
