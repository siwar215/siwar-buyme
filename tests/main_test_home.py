import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.home_screen import Home
from unittest import TestCase


class TestHome(TestCase):

    def setUp(self):
        f = open('./config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        if self.cfg["disable-notifications"]:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            self.driver = webdriver.Chrome(service=Service(driver_path), chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome(service=Service(driver_path))
        self.home_screen = Home(self.driver)

    def test_Once_logged_in(self):
        self.home_screen.goto_link(self.cfg['url']['buymehomepage'])
        self.home_screen.click_on_login_button()
        self.home_screen.login_valid_credentials()

    def test_search_for_gift(self):
        self.home_screen.goto_link(self.cfg['url']['buymehomepage'])
        self.home_screen.search_for_Gift()

    def tearDown(self):
        self.driver.quit()
