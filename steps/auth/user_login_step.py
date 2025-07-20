from interface.element_wait_then_click import element_wait_then_click
from interface.element_wait_then_fill import element_wait_then_fill
from pages.login_page import LoginPage


def user_login_step(login_page: LoginPage, username: str, password: str):
    """
    Performs the complete login step:
    1. Enters the username
    2. Enters the password
    3. Clicks the "Login" button
    """
    element_wait_then_fill(
        login_page, element=login_page._USERNAME_INPUT, text=username
    )
    element_wait_then_fill(
        login_page, element=login_page._PASSWORD_INPUT, text=password
    )
    element_wait_then_click(login_page, element=login_page._LOGIN_BUTTON)
