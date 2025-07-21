from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """
    Page Object for the checkout complete page
    https://www.saucedemo.com/checkout-complete.html
    """

    # Locators
    _COMPLETE_HEADER = (By.CSS_SELECTOR, 'h2[data-test="complete-header"]')
    _COMPLETE_TEXT = (By.CSS_SELECTOR, 'div[data-test="complete-text"]')
    _BACK_HOME_BUTTON = (By.CSS_SELECTOR, 'button[data-test="back-to-products"]')
