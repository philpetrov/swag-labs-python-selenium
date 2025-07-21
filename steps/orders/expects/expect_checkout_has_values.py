from selenium.webdriver.remote.webdriver import WebDriver

from interface.expect_element_has_text import expect_element_has_text
from logger import logger
from pages.checkout.checkout_step_two_page import CheckoutStepTwoPage
from utils.calculate_tax_and_total import calculate_tax_and_total


def expect_checkout_has_values(
    driver: WebDriver, product_name: str, product_price: str
):
    """
    Verifies that the checkout step two page displays
    correct item total, tax, and final total.

    :param driver: WebDriver instance
    :param product_name: Product name (used for logging)
    :param product_price: Expected product price as string, e.g. "$29.99"
    """

    checkout_step_two_page = CheckoutStepTwoPage(driver)

    expect_element_has_text(
        driver,
        element=checkout_step_two_page._ITEM_TOTAL_TXT,
        text=f"Item total: {product_price}",
    )

    price_val = float(product_price.replace("$", ""))
    expected_tax_str, expected_total_str = calculate_tax_and_total(price_val)

    expect_element_has_text(
        driver,
        element=checkout_step_two_page._TAX_TXT,
        text=expected_tax_str,
    )

    expect_element_has_text(
        driver,
        element=checkout_step_two_page._TOTAL_TXT,
        text=expected_total_str,
    )

    logger.info(
        f"✅ Checkout summary for '{product_name}' verified: "
        f"Item={product_price}, Tax={expected_tax_str}, Total={expected_total_str}"
    )
