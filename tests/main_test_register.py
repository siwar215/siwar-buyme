import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.registration_screen import Registration
from unittest import TestCase


class TestRegistration(TestCase):

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
        self.register_page = Registration(self.driver)

    def test_a_success_register(self):
        self.register_page.goto_link(self.cfg['url']['buymehomepage'])
        self.register_page.click_on_login_button()
        self.register_page.click_on_register()
        self.register_page.register()

    def test_if_email_valid(self):
        self.register_page.goto_link(self.cfg['url']['buymehomepage'])
        self.register_page.click_on_login_button()
        self.register_page.click_on_register()
        self.register_page.if_email_valid()

    def test_if_pass_valid(self):
        self.register_page.goto_link(self.cfg['url']['buymehomepage'])
        self.register_page.click_on_login_button()
        self.register_page.click_on_register()
        self.register_page.if_pass_valid()

    def test_if_pass_mismatched(self):
        self.register_page.goto_link(self.cfg['url']['buymehomepage'])
        self.register_page.click_on_login_button()
        self.register_page.click_on_register()
        self.register_page.if_pass_not_match()

    def test_if_firstname_correct(self):
        self.register_page.goto_link(self.cfg['url']['buymehomepage'])
        self.register_page.click_on_login_button()
        self.register_page.click_on_register()
        self.register_page.if_first_name_correct()

    def tearDown(self):
        self.driver.quit()





