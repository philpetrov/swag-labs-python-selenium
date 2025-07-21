from selenium.webdriver.remote.webdriver import WebDriver

from interface.wait_for_element_visible import wait_for_element_visible


def expect_element_has_text(driver: WebDriver, locator: tuple, expected_text: str):
    """
    Waits for an element to be visible and verifies its text content.

    :param driver: Selenium WebDriver instance.
    :param locator: Tuple of (By, selector) for the element.
    :param expected_text: The text the element is expected to have.
    """
    element = wait_for_element_visible(driver, locator)
    actual_text = element.text
    assert actual_text == expected_text, \
        f"Element with locator '{locator}' has incorrect text. " \
        f"Expected: '{expected_text}', but got: '{actual_text}'"