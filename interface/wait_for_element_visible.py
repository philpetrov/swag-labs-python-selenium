from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_visible(driver: WebDriver, element: tuple, timeout: int = 5):
    """
    Waits until the element located by the given locator is visible on the page.

    :param driver: Selenium WebDriver instance
    :param locator: Tuple of (By, selector)
    :param timeout: Timeout in seconds
    :return: The visible WebElement
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(element)
    )
