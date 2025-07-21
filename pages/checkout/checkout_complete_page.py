from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """
    Page Object for the checkout complete page https://www.saucedemo.com/checkout-complete.html
    """
    # Locators
    _CHECKOUT_COMPLETE_MESSAGE = (By.CSS_SELECTOR, 'h2[data-test="checkout_complete_container"]')
    _BACK_HOME_BUTTON = (By.CSS_SELECTOR, 'button[data-test="back-to-products"]')





