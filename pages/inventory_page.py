from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object for the inventory page https://www.saucedemo.com/inventory.html
    """
    # Locators
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    _ITEM_NAME = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
    _ITEM_PRICE = (By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]')
    _CART_BUTTON = (By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')


