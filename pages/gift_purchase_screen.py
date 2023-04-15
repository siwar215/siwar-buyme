import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Constants:
    for_someone_else = By.XPATH, "//div[@gtm='למישהו אחר']"
    receiver_name = By.XPATH, "//input[contains(@title, 'שם מקבל המתנה')]"
    celebration_event = By.XPATH, "//span[contains(@title, 'לאיזה אירוע')]"
    celebration_value = By.XPATH, "//li[@value='11']"
    send_grace_text = By.XPATH, "//textarea[@data-parsley-group='voucher-greeting']"
    upload_image = By.XPATH, "//input[@type='file']"
    continue_button = By.XPATH, "//button[@type='submit']"
    select_now = By.XPATH, "//div[@class='ember-view button button-now selected']"
    send_by_sms = By.XPATH, "//div[@class='circle-area']/*[name()='svg'][@gtm='method-sms']"

    receiver_mobile_number = By.ID, 'sms'
    sender_name = By.XPATH, "//input[@placeholder='שם שולח המתנה']"
    sender_mobile = By.XPATH, "//input[@placeholder='מספר נייד']"
    continue_to_payment_button = By.XPATH, "//button[@type='submit']"
    remove_media_mark = (By.XPATH, "//span[@class='remove-media']")


class sender_and_receiver(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.image_location = None
        self.base_page = None
        self.cfg = None

    def setUp(self):
        f = open('config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.image_location = self.cfg['upload']['gift_image']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.base_page = BasePage(self.driver)

    def scroll_to_bottom_screen(self):
        BasePage.scroll_page(self, "down")

    def gift_purchase(self):
        sender_and_receiver.scroll_to_bottom_screen(self)
        BasePage.wait_and_click_on_element(self, Constants.for_someone_else)
        BasePage.wait_and_enter_text(self, Constants.receiver_name, "Siwar")
        BasePage.wait_and_click_on_element(self, Constants.celebration_event)
        BasePage.wait_and_select_element(self, Constants.celebration_value)
        BasePage.clear_text(self, Constants.send_grace_text)
        BasePage.wait_and_enter_text(self, Constants.send_grace_text, "Thank you very much for the great "
                                                                      "investment!Here is a special little gift for "
                                                                      "you")

    def upload_a_picture(self):
        # BasePage.wait_and_enter_text(self, Constants.upload_image, self.image_location)
        BasePage.wait_and_enter_text(self, Constants.upload_image, "/Users/siwarkhateeb/Downloads/BuyMeGift.jpeg")
        BasePage.wait_for_element_to_appear(self, Constants.remove_media_mark)
        BasePage.wait_and_click_on_element(self, Constants.continue_button)

    def enter_order_details(self):
        self.driver.execute_script(f"window.scrollBy(0, 400);")
        BasePage.wait_and_click_on_element(self, Constants.select_now)
        BasePage.wait_and_click_on_element(self, Constants.send_by_sms)
        BasePage.wait_and_enter_text(self, Constants.receiver_mobile_number, "0540000000")
        BasePage.wait_and_enter_text(self, Constants.sender_name, "Siwar Khateeb")
        BasePage.wait_and_enter_text(self, Constants.sender_mobile, "0547227042")
        BasePage.wait_and_click_on_element(self, Constants.continue_to_payment_button)
