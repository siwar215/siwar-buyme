import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.registration_screen import Registration
from unittest import TestCase


class TestRegistration(TestCase):

    def setUp(self):
        f = open('config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.register_page = Registration(self.driver)

    def test_a_success_register(self):
        self.register_page.goto_link(self.cfg['url']['buymehomepage'])
        self.register_page.click_on_login_button()
        self.register_page.click_on_register()


