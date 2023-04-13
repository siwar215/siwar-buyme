import logging

from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    # Configure logging to write to a file
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(
        filename="BuyMe_log.txt",
        filemode='a',
        format="%(asctime)s, %(name)s %(levelname)s %(message)s \n",
        datefmt="%H:%M:%S",
        level=logging.ERROR)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator, value):
        try:
            self.wait.until(EC.element_to_be_clickable((locator, value))).click()
        except TimeoutException as e:
            logging.exception(str(e))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_element(self, locator, value):
        try:
            self.driver.find_element(locator, value).click()
        except TimeoutException as e:
            logging.exception(str(e))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)




    def add_text_to_element(self, locator, value, text):
        self.driver.find_element(locator, value).send_keys(text)
