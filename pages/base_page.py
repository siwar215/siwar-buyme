import logging

from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType

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

    def goto_link(self, link):
        try:
            self.driver.get(link)
            self.wait.until(EC.url_to_be(link))
        except Exception as e:
            logging.exception(str(e))
            ss_png = self.driver.get_screenshot_as_png()
            allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)

    def wait_and_click_on_element(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator)).click()
        except Exception as e:
            logging.exception(str(e))
            ss_png = self.driver.get_screenshot_as_png()
            allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)

    def wait_and_enter_text(self, locator, text):
        try:
            self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)
        except Exception as e:
            logging.exception(str(e))
            ss_png = self.driver.get_screenshot_as_png()
            allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)

    def wait_and_click_on_below_element(self, element, elem_type, elem_val):
        try:
            relative_element = self.wait.until(EC.element_to_be_clickable(element))
            self.driver.find_element(locate_with(elem_type, elem_val).below(relative_element)).click()
        except Exception as e:
            logging.exception(str(e))
            ss_png = self.driver.get_screenshot_as_png()
            allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)

    def wait_and_verify_text(self, locator, expected_text):
        try:
            text = self.wait.until(EC.presence_of_element_located(locator))
            if expected_text not in text:
                ss_png = self.driver.get_screenshot_as_png()
                allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)
            else:
                logging.info(f"Found String {expected_text} in {text}")
                ss_png = self.driver.get_screenshot_as_png()
                allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)
                return text
        except Exception as e:
            logging.exception(str(e))
            ss_png = self.driver.get_screenshot_as_png()
            allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)




