from selenium.webdriver.common.by import By

from pages.base_page import BasePage




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



