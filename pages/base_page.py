import logging
import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
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
                logging.debug(f"String '{expected_text}' wasn't found in '{text}'")
                self.save_screenshot(f"String_{expected_text}_wasn't_found")
            else:
                logging.info(f"Found String {expected_text} in {text}")
                self.save_screenshot(f"String_{expected_text}_wasn't_found")
                return text
        except TimeoutException:
            logging.debug(f"Timed out waiting for element with locator '{locator}'")
        except NoSuchElementException:
            logging.debug(f"Element with locator '{locator}' not found")
        except Exception as e:
            logging.exception(str(e))
            # Capture screenshot only when necessary
            # self.save_screenshot("wait_and_verify_text-Failed")
            ss_png = self.driver.get_screenshot_as_png()
            allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)

    def save_screenshot(self, filename):
        # Capture screenshot using Selenium's driver.save_screenshot
        self.driver.save_screenshot(filename)
        logging.info(f"Screenshot saved as '{filename}'")

    # def scroll_page(self, direction: str):
    #     try:
    #         if direction == "up":
    #             # Scroll to the top of the page
    #             self.driver.execute_script("window.scrollTo(0, 0);")
    #             time.sleep(1)
    #         elif direction == "down":
    #             # Scroll to the bottom of the page
    #             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #             time.sleep(1)
    #     except Exception as e:
    #         # Invalid direction parameter
    #         logging.exception(str(e))
    #         self.save_screenshot("scroll_page-Failed")



    def assert_url(self, link):
        try:
            self.wait.until(EC.url_to_be(link))
        except TimeoutException:
            logging.error(f"Timed out waiting for URL to be: {link}")
            self.save_screenshot("verify_link-Failed")

    def scroll_search_and_click_element(self, locator, times):
        scroll_amount = 400
        for i in range(times):
            try:
                self.wait.until(EC.presence_of_element_located(locator))
                ActionChains(self.driver).move_to_element(locator).click().perform()
                return
            except Exception as e:
                self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                logging.exception(str(e))
                logging.error(f"Element {locator} wasn't found after {times} times")
                ss_png = self.driver.get_screenshot_as_png()
                allure.attach(ss_png, name="Screenshot", attachment_type=AttachmentType.PNG)