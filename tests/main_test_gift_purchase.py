import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.gift_purchase_screen import sender_and_receiver
from pages.pick_business_screen import Pick_Business
from unittest import TestCase


class TestGiftPurchase(TestCase):

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
        self.pick_business_screen = Pick_Business(self.driver)
        self.gift_purchase_screen = sender_and_receiver(self.driver)

    def test_gift_purchase(self):
        self.pick_business_screen.goto_link(self.cfg['url']['buymehomepage'])
        self.pick_business_screen.choose_business_gift_card()
        self.gift_purchase_screen.gift_purchase()
        self.gift_purchase_screen.upload_a_picture()
        self.gift_purchase_screen.enter_order_details()

    def test_to_verify_only_gift_purchase_page(self):
        self.gift_purchase_screen.goto_link(self.cfg['url']['sender_and_receiver_page'])
        self.gift_purchase_screen.gift_purchase()
        self.gift_purchase_screen.upload_a_picture()
        self.gift_purchase_screen.enter_order_details()

    def tearDown(self):
        self.driver.quit()
