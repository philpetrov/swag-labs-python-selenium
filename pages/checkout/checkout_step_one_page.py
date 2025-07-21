from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """
    Page Object for the checkout step one page https://www.saucedemo.com/checkout-step-one.html
    """
    # Locators
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[data-test="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[data-test="lastName"]')
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, 'input[data-test="postalCode"]')

    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[data-test="continue"]')




