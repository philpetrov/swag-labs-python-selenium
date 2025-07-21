from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """
    Base class for all pages.
    """

    # Common locators
    _ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    CART_BUTTON = (By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
    CANCEL_BUTTON = (By.CSS_SELECTOR, 'button[data-test="cancel"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver
