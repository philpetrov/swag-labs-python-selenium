from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the login page https://www.saucedemo.com/
    Used as a static locator holder.
    """

    _USERNAME_INPUT = (By.CSS_SELECTOR, '[data-test="username"]')
    _PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-test="password"]')
    _LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
