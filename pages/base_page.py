import logging

from allure_commons.types import AttachmentType
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Configure logging to write to a file
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(
    filename="BuyMe_log.txt",
    filemode='a',
    format="%(asctime)s, %(name)s %(levelname)s %(message)s \n",
    datefmt="%H:%M:%S",
    level=logging.ERROR)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_url(self, url):
        try:
            self.driver.get(url)
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def get_current_url(self):
        try:
            return self.driver.current_url
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def wait_for_url(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def wait_for_element(self, locator, value):
        try:
            self.wait.until(EC.element_to_be_clickable((locator, value))).click()
        except Exception as e:
            logger.exception(str(e))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_elements(self, locator):
        try:
            return self.driver.find_elements(locator)
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    def click_element(self, locator, value):
        try:
            self.driver.find_element(locator, value).click()
        except Exception as e:
            logger.exception(str(e))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def send_text(self, locator, value, text):
        try:
            self.driver.find_element(locator, value).send_keys(text)
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_element_and_submit(self, locator, value):
        try:
            self.find_web_element(locator, value).submit()
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_web_element(self, locator, value):
        try:
            element = self.driver.find_element(locator, value)
            return element
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_then_return_web_element_text(self, locator, value):
        try:
            element = self.driver.find_element(locator, value)
            return element.text
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_element_below(self, locator, value, relative_type, relative_value):
        try:
            self.driver.find_element(locate_with(locator, value).below(
                self.find_web_element(relative_type, relative_value))).click()
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def wait_4_text_in_element(self, locator, text):
        try:
            self.wait.until(EC.text_to_be_present_in_element(locator, text))
        except Exception as exception:
            logger.error(f"An exception occurred: {exception}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


