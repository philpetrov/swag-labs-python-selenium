# import time

import pytest

from interface.go_to_url import go_to_url
from steps.auth.expects.expect_user_logged_in import expect_user_logged_in
from steps.auth.user_login_step import user_login_step
from steps.orders.create_order_step import create_order_step
from steps.orders.expects.expect_order_created import expect_order_created
from utils.user_data_generator import generate_user_data


@pytest.mark.SC1
@pytest.mark.parametrize(
    "product_name",
    [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
    ],
)
def test_successful_create_order(
    driver, standard_user_credentials, base_url, product_name
):
    """
    Test case: Successful create order for different products.
    Steps:
    1. Go to the login page.
    2. Authorize as a standard user.
    3. Add a specified product to the cart and proceed through checkout.
    4. Verify that the order is completed successfully.
    """
    username, password = standard_user_credentials
    user_data = generate_user_data()

    go_to_url(driver, base_url)

    user_login_step(driver, username, password)

    expect_user_logged_in(driver)

    create_order_step(
        driver,
        product_name=product_name,
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        postal_code=user_data["postal_code"],
    )

    expect_order_created(driver)

    # time.sleep(120) # This can be removed for automated runs
