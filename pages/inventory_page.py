from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object for the inventory page https://www.saucedemo.com/inventory.html
    """
    # Locators
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    CART_ITEM = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')

