from selenium.webdriver.remote.webdriver import WebDriver

from interface.expect_element_has_text import expect_element_has_text
from interface.wait_for_element_visible import wait_for_element_visible
from pages.checkout.checkout_complete_page import CheckoutCompletePage


def expect_order_created(driver: WebDriver):
    """
    Verifies that the order has been successfully created.

    This function checks for the following on the checkout complete page:
    1. The visibility of the "Back Home" button.
    2. The presence and text of the "Thank you for your order!" header.
    3. The presence and text of the order dispatch confirmation message.
    """
    checkout_complete_page = CheckoutCompletePage(driver)

    # 1. Verify the "Back Home" button is visible
    wait_for_element_visible(driver, checkout_complete_page._BACK_HOME_BUTTON)

    # 2. Verify the header text
    expect_element_has_text(
        driver,
        checkout_complete_page._COMPLETE_HEADER,
        "Thank you for your order!"
    )

    # 3. Verify the completion message text
    expect_element_has_text(
        driver,
        checkout_complete_page._COMPLETE_TEXT,
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    )