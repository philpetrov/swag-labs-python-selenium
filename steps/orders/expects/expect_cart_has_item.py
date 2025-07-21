from selenium.webdriver.remote.webdriver import WebDriver

from interface.expect_element_has_text import expect_element_has_text
from logger import logger
from pages.cart_page import CartPage


def expect_cart_has_item(driver: WebDriver, product_name: str, expected_price: str):
    """
    Verifies that a specific item is present in the cart with the correct price.

    :param driver: WebDriver instance
    :param product_name: Name of the product (e.g. "Sauce Labs Backpack")
    :param expected_price: Expected price as string (e.g. "$29.99")
    """

    cart_page = CartPage(driver)

    expect_element_has_text(driver, element=cart_page._PRODUCT_NAME, text=product_name)

    product_price_in_cart = cart_page.get_price_by_product_name(product_name)
    assert (
        expected_price == product_price_in_cart
    ), (
        f"❌ Price mismatch in cart: expected '{expected_price}', "
        f"got '{product_price_in_cart}'"
    )

    logger.info(
        f"✅ Product '{product_name}' verified in cart with price "
        f"{expected_price}"
    )
