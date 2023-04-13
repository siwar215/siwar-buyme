import json
import time

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
    register_first_name = By.XPATH, "//input[@placeholder='שם פרטי']"
    register_email = By.XPATH, "//input[@placeholder='מייל']"
    register_password = By.ID, "valPass"
    register_password_conf = By.XPATH, "//input[@placeholder='אימות סיסמה']"
    agree_radio = By.XPATH, "//span[@class='circle']"
    submit = By.XPATH, "//button[@type='submit']"
    no_entery = By.CLASS_NAME, "parsley-required"
    passwords_mismached_error = By.CLASS_NAME, "parsley-equalto"


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
        BasePage.wait_and_click_on_below_element(self, Constants.register, Constants.register_type,
                                                 Constants.register_value)

    def register(self):
        BasePage.wait_and_enter_text(self, Constants.register_first_name, "Siwar_khateeb")
        BasePage.wait_and_enter_text(self, Constants.register_email, "siwartest@email.com")
        BasePage.wait_and_enter_text(self, Constants.register_password, "Password")
        BasePage.wait_and_enter_text(self, Constants.register_password_conf, "Password")
        BasePage.wait_and_click_on_element(self, Constants.agree_radio)
        BasePage.wait_and_click_on_element(self, Constants.submit)

    def if_email_valid(self):
        BasePage.wait_and_enter_text(self, Constants.register_first_name, "Siwar_khateeb")
        BasePage.wait_and_enter_text(self, Constants.register_email, "empty")
        BasePage.wait_and_click_on_element(self, Constants.submit)
        BasePage.wait_and_verify_text(self, Constants.no_entery, "ערך זה דרוש")

    def if_pass_valid(self):
        # 1.Verifying when the password fields are empty
        BasePage.wait_and_enter_text(self, Constants.register_first_name, "Siwar_khateeb")
        BasePage.wait_and_enter_text(self, Constants.register_password, "")
        BasePage.wait_and_enter_text(self, Constants.register_password_conf, "")
        BasePage.wait_and_click_on_element(self, Constants.submit)
        BasePage.wait_and_verify_text(self, Constants.register_password, "ערך זה דרוש.")
        BasePage.wait_and_verify_text(self, Constants.register_password_conf, "ערך זה דרוש.")

    def if_pass_not_match(self):
        # 2.Verifying when the enter password and Re-enter password fields doesn't match
        BasePage.wait_and_enter_text(self, Constants.register_password, "Siwar12")
        BasePage.wait_and_enter_text(self, Constants.register_password_conf, "Siwar123")
        BasePage.wait_and_click_on_element(self, Constants.submit)
        BasePage.wait_and_verify_text(self, Constants.passwords_mismached_error, "הסיסמאות לא זהות, אולי זה מהתרגשות :)")


