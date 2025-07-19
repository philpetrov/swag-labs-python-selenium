from pages.login_page import LoginPage


def login(login_page: LoginPage, username: str, password: str):
    """
    Performs the complete login step:
    1. Enters the username
    2. Enters the password
    3. Clicks the "Login" button
    """
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()