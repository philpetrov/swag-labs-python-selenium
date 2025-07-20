
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def element_wait_then_click(page, element: tuple, timeout: int = 5):
    """
    Waits until the element located by the given locator is clickable, then clicks it.
    """
    element = WebDriverWait(page.driver, timeout).until(
        EC.element_to_be_clickable(element)
    )
    element.click()
