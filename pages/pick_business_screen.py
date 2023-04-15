import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Constants:
    search_button = By.XPATH, "//a[@class='ember-view bm-btn no-reverse main md ember-view']"
    business_name = By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/ul/div[53]/a/div/div[3]"
    gift_value = By.XPATH, '//input[@placeholder="הכנס סכום"]'
    card_submit = By.XPATH, '//button[@type="submit"]'


class Pick_Business(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.base_page = None
        self.cfg = None

    def setUp(self):
        f = open('config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.base_page = BasePage(self.driver)

    def choose_business_gift_card(self):
        # clicking on the search button to view all the businesses on BuyMe website
        BasePage.wait_and_click_on_element(self, Constants.search_button)
        BasePage.assert_url(self, "https://buyme.co.il/search")
        BasePage.scroll_search_and_click_element(self, Constants.business_name, 10)
        BasePage.wait_and_click_on_element(self, Constants.business_name)
        BasePage.wait_and_enter_text(self, Constants.gift_value, "1000")
        BasePage.wait_and_click_on_element(self, Constants.card_submit)
