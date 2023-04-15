import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.base_page import BasePage


class sender_and_receiver(BasePage):

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

    def scroll_to_bottom_screen(self):
        BasePage.scroll_page(self, "down")
