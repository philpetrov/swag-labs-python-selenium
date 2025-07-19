import time

from login_page import LoginPage
from steps.auth.login_step import login, login_step


def test_successful_login(driver):
    """
    Test case: Successful login.
    Steps:
    1. Open the login page.
    2. Enter valid credentials ('standard_user', 'secret_sauce').
    3. Click the "Login" button.
    4. Verify that the URL has changed to the inventory page.
    """
    login_page = LoginPage(driver)
    login_page.open()

    login_step(login_page, "standard_user", "secret_sauce")

    time.sleep(10)

    assert "inventory.html" in login_page.get_current_url(), "Login failed or redirected to the wrong page"