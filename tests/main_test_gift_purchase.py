import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.gift_purchase_screen import sender_and_receiver
from pages.pick_business_screen import Pick_Business
from unittest import TestCase


class TestGiftPurchase(TestCase):

    def setUp(self):
        f = open('../config.json', 'r')
        config_json = json.load(f)
        self.cfg = config_json
        driver_path = self.cfg['drivers']['chrome']
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.pick_business_screen = Pick_Business(self.driver)
        self.gift_purchase_screen = sender_and_receiver(self.driver)

    def test_pick_business2(self):
        self.gift_purchase_screen.scroll_to_bottom_screen()

