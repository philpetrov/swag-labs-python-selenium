from selenium.webdriver.remote.webdriver import WebDriver


def go_to_url(driver: WebDriver, url: str):
    """
    Navigates the browser to the specified URL.

    :param driver: Selenium WebDriver instance.
    :param url: The URL to navigate to.
    """
    driver.get(url)
