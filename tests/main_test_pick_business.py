import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.pick_business_screen import Pick_Business
from unittest import TestCase


class TestPickBusiness(TestCase):

    def setUp(self):
        f = open('../config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.pick_business_screen = Pick_Business(self.driver)

    def test_pick_business(self):
        self.pick_business_screen.goto_link(self.cfg['url']['buymehomepage'])
        self.pick_business_screen.choose_business_gift_card()
