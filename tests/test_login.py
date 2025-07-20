import pytest
from pages.login_page import LoginPage
from steps.auth.expects.expect_user_logged_in import expect_user_logged_in
from steps.auth.user_login_step import user_login_step
from interface.go_to_url import go_to_url

@pytest.mark.L1
def test_successful_login(driver, standard_user_credentials, base_url):
    """
    Test case: Successful login.
    Steps:
    1. Open the login page.
    2. Enter valid credentials.
    3. Click the "Login" button.
    4. Verify that the URL has changed to the inventory page.
    """
    username, password = standard_user_credentials

    login_page = LoginPage(driver)

    go_to_url(driver, base_url)

    user_login_step(login_page, username, password)

    expect_user_logged_in(driver)
