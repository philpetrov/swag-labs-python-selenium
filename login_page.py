from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the login page https://www.saucedemo.com/
    """

    # Locators for elements on the login page.
    # Using the data-test attribute is a reliable practice.
    _USERNAME_INPUT = (By.CSS_SELECTOR, '[data-test="username"]')
    _PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-test="password"]')
    _LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')

    def __init__(self, driver):
        super().__init__(driver, "https://www.saucedemo.com/")

    def enter_username(self, username: str):
        self.find_element(self._USERNAME_INPUT).send_keys(username)

    def enter_password(self, password: str):
        self.find_element(self._PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.find_element(self._LOGIN_BUTTON).click()