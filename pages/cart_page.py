from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    """
    Page Object for the cart page https://www.saucedemo.com/cart.html
    """
    # Locators
    _PRODUCT_NAME = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
    _PRODUCT_PRICE = (By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]')   
    _REMOVE_BUTTON = (By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-backpack"]')  
    _CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, 'button[data-test="continue-shopping"]') 
    _CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'button[data-test="checkout"]')

    def get_price_by_product_name(self, product_name: str, timeout: int = 5) -> str:
        """
        Finds the product price by name in the Cart page.

        :param product_name: Product name (e.g., "Sauce Labs Backpack")
        :param timeout: Timeout in seconds
        :return: Price string (e.g., "$29.99")
        """
        xpath = (
            f'//div[@class="cart_item" and .//div[@data-test="inventory-item-name" '
            f'and normalize-space(text())="{product_name}"]]//div[@data-test="inventory-item-price"]'
        )
        price_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return price_element.text.strip()
