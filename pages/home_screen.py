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
    drop_price = By.XPATH, "//span[@title='סכום']"
    drop_amount = By.XPATH, "//span[contains(text(), '500-750')]"
    drop_area = By.XPATH, "//span[@title='אזור']"
    drop_subarea = By.XPATH, "//span[text()='צפון']"
    drop_category = By.XPATH, "//span[@title='קטגוריה']"
    drop_subcategory = By.XPATH, "//span[contains(text(), 'גיפט קארד למסעדות')]"
    button_find_gift = By.XPATH, "//a[@rel='nofollow']"


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

    def search_for_Gift(self):
        self.driver.execute_script(f"window.scrollBy(0, 300);")
        BasePage.wait_and_click_on_element(self, Constants.drop_price)
        BasePage.wait_and_click_on_element(self, Constants.drop_amount)
        BasePage.wait_and_click_on_element(self, Constants.drop_area)
        BasePage.wait_and_click_on_element(self, Constants.drop_subarea)
        BasePage.wait_and_click_on_element(self, Constants.drop_category)
        BasePage.wait_and_click_on_element(self, Constants.drop_subcategory)
        BasePage.wait_and_click_on_element(self, Constants.button_find_gift)
