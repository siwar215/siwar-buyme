import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Constants:
    login_register = By.LINK_TEXT, "כניסה / הרשמה"
    login_email = By.XPATH, "//input[@placeholder='מייל']"
    login_pass = By.XPATH, "//input[@placeholder='סיסמה']"
    submit = By.XPATH, "//button[@type='submit']"


class Home(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def setUp(self):
        f = open('config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.base_page = BasePage(self.driver)

    # Once logged in by inserting a valid credentials
    def click_on_login_button(self):
        BasePage.wait_and_click_on_element(self, Constants.login_register)

    def login_valid_credentials(self):
        BasePage.wait_and_enter_text(self, Constants.login_email, "siwarkhateeb215@gmail.com")
        BasePage.wait_and_enter_text(self, Constants.login_pass, "Password123")
        BasePage.wait_and_click_on_element(self, Constants.submit)
