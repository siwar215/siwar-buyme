import json
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.base_page import BasePage


class TestRegistration(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup")
        f = open('config.json', 'r')  # TODO: move to env ?
        config_json = json.load(f)
        cls.cfg = config_json
        driver_path = cls.cfg['drivers']['chrome']
        cls.driver = webdriver.Chrome(service=Service(driver_path))
        cls.base_page = BasePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_a_success_register(self):
        self.base_page.run_test()
        # base.goto_link(driver, base_page.datajson['urls']['buymehome'])
        # self.home_page.click_on_login()
        # self.home_page.click_on_register()
        # self.home_page.verify_title_Registration()
        # self.register_page.register_success()
