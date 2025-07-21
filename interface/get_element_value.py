from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_element_value(page, element: tuple, timeout: int = 5) -> str:
    """
    Waits until the element located by the given locator is visible, then returns its text content.
    
    :param page: a page object containing the driver
    :param element: element locator in the form of a tuple (By, value)
    :param timeout: maximum waiting time
    :return: text content of the element
    """
    web_element = WebDriverWait(page.driver, timeout).until(
        EC.visibility_of_element_located(element)
    )
    return web_element.text.strip()
