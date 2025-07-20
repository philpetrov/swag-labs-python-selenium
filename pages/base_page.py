from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """
    Base class for all pages.
    """

    # Common locators
    _ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver