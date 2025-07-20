from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

def element_wait_then_fill(page, element: tuple, text: str, timeout: int = 5):
    """
    Waits until the element located by the given locator is visible, then fills it with the specified text.
    """
    element = WebDriverWait(page.driver, timeout).until(
        EC.visibility_of_element_located(element)
    )
    element.send_keys(text)
