from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Constants:
    register_first_name = By.XPATH, "//input[@placeholder='שם פרטי']"
    register_email = By.XPATH, "//input[@placeholder='מייל']"
    register_password = By.ID, "valPass"
    register_password_conf = By.XPATH, "//input[@placeholder='אימות סיסמה']"
    agree_radio = By.XPATH, "//span[@class='circle']"
    submit = By.XPATH, "//button[@type='submit']"
    email_required_error = By.ID, "parsley-id-27"  # "//input[@data-parsley-id='23']" #By.CLASS_NAME, "parsley-required"
    password_mismach_error = By.CLASS_NAME, "parsley-equalto"


class Registration(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def register_success(self):
        BasePage.wait_and_enter_text(self, Constants.register_first_name, "register_success")
        BasePage.wait_and_enter_text(self, Constants.register_email, "test@email.com")
        BasePage.wait_and_enter_text(self, Constants.register_password, "Password")
        BasePage.wait_and_enter_text(self, Constants.register_password_conf, "Password2")
        BasePage.wait_and_click_on_element(self, Constants.agree_radio)
