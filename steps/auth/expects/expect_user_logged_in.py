from interface.get_current_url import get_current_url

def expect_user_logged_in(driver, expected_path: str = "inventory.html"):
    """
    Asserts that the user is logged in by verifying the URL contains the expected path.
    """
    current_url = get_current_url(driver)
    assert expected_path in current_url, f"Expected to be on '{expected_path}', but current URL is '{current_url}'"
