from interface.wait_for_element_visible import wait_for_element_visible


def expect_login_failed(driver, element, timeout: int = 5):
    """
    Asserts that the login failed by checking if the error message is visible.
    """
    wait_for_element_visible(driver, element, timeout)
