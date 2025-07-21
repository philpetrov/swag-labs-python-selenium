import pytest

from interface.go_to_url import go_to_url
from pages.login_page import LoginPage
from steps.auth.expects.expect_user_logged_in import expect_user_logged_in
from steps.auth.expects.expect_user_login_failed import expect_login_failed
from steps.auth.user_login_step import user_login_step


@pytest.mark.L1
def test_successful_user_login(driver, standard_user_credentials, base_url):
    """
    Test case: Successful login.
    Steps:
    1. Go to the login page.
    2. Enter valid credentials.
    3. Click the "Login" button.
    4. Verify that the URL has changed to the inventory page.
    """
    username, password = standard_user_credentials

    go_to_url(driver, base_url)

    user_login_step(driver, username, password)

    expect_user_logged_in(driver)


@pytest.mark.L2
@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "wrong_password"),
        ("invalid_user", "secret_sauce"),
        ("", ""),
    ],
)
def test_failed_user_login(driver, base_url, username, password):
    """
    Negative test cases for login:
    - Incorrect username
    - Incorrect password
    - Both fields empty
    """
    go_to_url(driver, base_url)

    user_login_step(driver, username, password)

    login_page = LoginPage(driver)

    expect_login_failed(driver, login_page._ERROR_MESSAGE)
