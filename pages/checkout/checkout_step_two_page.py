from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    """
    Page Object for the checkout step one page https://www.saucedemo.com/checkout-step-two.html
    """
    # Locators
    FINISH_BUTTON = (By.CSS_SELECTOR, 'button[data-test="finish"]')





