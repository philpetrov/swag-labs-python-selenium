from selenium.webdriver.common.by import By

class LoginPage:
    """
    Page Object for the login page https://www.saucedemo.com/
    Used as a static locator holder.
    """

    url = "https://www.saucedemo.com/"

    # Locators
    _USERNAME_INPUT = (By.CSS_SELECTOR, '[data-test="username"]')
    _PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-test="password"]')
    _LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')

    def __init__(self, driver):
        self.driver = driver
