from selenium.webdriver.remote.webdriver import WebDriver


def get_current_url(driver: WebDriver) -> str:
    """
    Returns the current URL of the page loaded in the browser.

    :param driver: Selenium WebDriver instance
    :return: Current page URL as a string
    """
    return driver.current_url
