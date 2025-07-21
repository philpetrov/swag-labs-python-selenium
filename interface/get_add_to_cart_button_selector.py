from selenium.webdriver.common.by import By


def get_add_to_cart_button_selector(product_name: str):
    """
    Returns the locator of the "Add to cart" button by the product name.
    Example: "Sauce Labs Backpack" → "sauce-labs-backpack"
    """
    normalized_name = product_name.lower().replace(" ", "-")
    data_test_value = f"add-to-cart-{normalized_name}"
    return (By.CSS_SELECTOR, f'button[data-test="{data_test_value}"]')
