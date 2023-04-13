import json
from lib2to3.pgen2 import driver
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.base_page import BasePage
from pages.registration_screen import Registration
from unittest import TestCase


class TestRegistration(TestCase):

    def setUp(self):
        f = open('config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.base_page = BasePage(self.driver)

    def test_a_success_register(self):
        BasePage.goto_link(self.base_page, self.cfg['url']['buymehomepage'])

    # @classmethod
    # def setUpClass(cls):
    #
    #     f = open('/Users/siwarkhateeb/Downloads/siwar-buyme/config.json', 'r')
    #     config_json = json.load(f)
    #     cls.cfg = config_json
    #     driver_path = cls.cfg['drivers']['chrome']
    #     cls.driver = webdriver.Chrome(service=Service(driver_path))
    #     cls.base_page = BasePage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
