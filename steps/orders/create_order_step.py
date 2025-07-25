from interface.element_wait_then_click import element_wait_then_click
from interface.element_wait_then_fill import element_wait_then_fill
from interface.get_add_to_cart_button_selector import \
    get_add_to_cart_button_selector
from logger import logger
from pages.cart_page import CartPage
from pages.checkout.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from steps.orders.expects.expect_cart_has_item import expect_cart_has_item
from steps.orders.expects.expect_checkout_has_values import \
    expect_checkout_has_values


def create_order_step(
    driver, product_name: str, first_name: str, last_name: str, postal_code: str
):
    """
    Performs the create order step:
    1. Add first item to the cart.
    2. Verify that the first item is in the cart.
    3. Go to the cart page.
    4. Verify that the first item is in the cart.
    5. Checkout
    6. Provide personal data and postal code
    7. Verify that the order is completed successfully.
    """

    inventory_page = InventoryPage(driver)
    item_price_at_inventory_page = inventory_page.get_price_by_product_name(
        product_name
    )
    logger.info(
        f"Price of item at the inventory page '{product_name}': "
        f"{item_price_at_inventory_page}"
    )
    element_wait_then_click(
        inventory_page, element=get_add_to_cart_button_selector(product_name)
    )
    element_wait_then_click(inventory_page, element=inventory_page._CART_BUTTON)

    cart_page = CartPage(driver)
    expect_cart_has_item(
        driver, product_name=product_name, expected_price=item_price_at_inventory_page
    )
    element_wait_then_click(cart_page, element=cart_page._CHECKOUT_BUTTON)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    element_wait_then_fill(
        checkout_step_one_page,
        element=checkout_step_one_page._FIRST_NAME_INPUT,
        text=first_name,
    )
    element_wait_then_fill(
        checkout_step_one_page,
        element=checkout_step_one_page._LAST_NAME_INPUT,
        text=last_name,
    )
    element_wait_then_fill(
        checkout_step_one_page,
        element=checkout_step_one_page._POSTAL_CODE_INPUT,
        text=postal_code,
    )

    element_wait_then_click(
        checkout_step_one_page, element=checkout_step_one_page._CONTINUE_BUTTON
    )
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    expect_checkout_has_values(
        driver, product_name=product_name, product_price=item_price_at_inventory_page
    )
    element_wait_then_click(
        checkout_step_two_page, element=checkout_step_two_page._FINISH_BUTTON
    )
