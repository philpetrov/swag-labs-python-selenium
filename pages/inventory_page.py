from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object for the inventory page https://www.saucedemo.com/inventory.html
    """

    # Locators
    _ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        'button[data-test="add-to-cart-sauce-labs-backpack"]',
    )
    _ITEM_NAME = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
    _ITEM_PRICE = (By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]')
    _CART_BUTTON = (By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')

    def get_price_by_product_name(self, product_name: str, timeout: int = 5) -> str:
        """
        Finds the product price by name on the Inventory page.

        :param product_name: Product name (e.g., "Sauce Labs Backpack")
        :param timeout: Timeout in seconds
        :return: Price string (e.g., "$29.99")
        """
        xpath = (
            f'//div[@class="inventory_item" and '
            f'.//div[@data-test="inventory-item-name" and '
            f'normalize-space(text())="{product_name}"]]'
            f'//div[@data-test="inventory-item-price"]'
        )
        price_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return price_element.text.strip()
