from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page Object for the cart page https://www.saucedemo.com/cart.html
    """
    # Locators
    PRODUCT_NAME = (By.CSS_SELECTOR, 'button[data-test="inventory-item-name"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]')   
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-backpack"]')  
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, 'button[data-test="continue-shopping"]') 
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'button[data-test="checkout"]')



