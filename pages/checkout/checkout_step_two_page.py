from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    """
    Page Object for the checkout step one page
    https://www.saucedemo.com/checkout-step-two.html
    """

    # Locators
    _FINISH_BUTTON = (By.CSS_SELECTOR, 'button[data-test="finish"]')
    _CANCEL_BUTTON = (By.CSS_SELECTOR, 'button[data-test="cancel"]')
    _ITEM_TOTAL_TXT = (By.CSS_SELECTOR, 'div[data-test="subtotal-label"]')
    _TAX_TXT = (By.CSS_SELECTOR, 'div[data-test="tax-label"]')
    _TOTAL_TXT = (By.CSS_SELECTOR, 'div[data-test="total-label"]')