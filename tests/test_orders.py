import time
import pytest

from interface.go_to_url import go_to_url
from pages.login_page import LoginPage
from steps.auth.expects.expect_user_logged_in import expect_user_logged_in
from steps.auth.user_login_step import user_login_step
from steps.orders.create_order_step import create_order_step


@pytest.mark.SC1
def test_successful_create_order(driver, standard_user_credentials, base_url):
    """
    Test case: Successful create order.
    Steps:
    1. Go to the login page.
    2. Authorization as user
    4. Add first item to the cart.
    5. Verify that the first item is in the cart.
    6. Go to the cart page.
    7. Verify that the first item is in the cart.
    8. Checkout
    9. Provide personal data and postal code
    10. Verify that the order is completed successfully.
    """
    username, password = standard_user_credentials

    go_to_url(driver, base_url)

    user_login_step(driver, username, password)

    expect_user_logged_in(driver)

    create_order_step(driver, product_name="Sauce Labs Backpack", first_name="John", last_name="Doe", postal_code="123456")

    expect_order_created(driver)

    time.sleep(120)



    