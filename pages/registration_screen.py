from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get('https://buyme.co.il')

    def click_register_area(self):
        self.click_element(By.LINK_TEXT, "כניסה / הרשמה")

    def wait_for_registration_form(self):
        self.wait_for_element(By.XPATH, "//span[text()='thisisatest']")