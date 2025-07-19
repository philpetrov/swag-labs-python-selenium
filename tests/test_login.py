
from pages.login_page import LoginPage
from steps.auth.login_step import login


def test_successful_login(driver, standard_user_credentials):
    """
    Test case: Successful login.
    Steps:
    1. Open the login page.
    2. Enter valid credentials from environment variables.
    3. Click the "Login" button.
    4. Verify that the URL has changed to the inventory page.
    """
    username, password = standard_user_credentials
    login_page = LoginPage(driver)
    login_page.open()

    login(login_page, username, password)

    assert "inventory.html" in login_page.get_current_url(), "Login failed or redirected to the wrong page"