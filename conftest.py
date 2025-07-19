import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """
    A pytest fixture using Selenium Manager (since Selenium 4.10+).
    Automatically detects installed Chrome and uses matching chromedriver.
    """
    options = Options()
    service = ChromeService()  # No need to manually manage driver path
    web_driver = webdriver.Chrome(service=service, options=options)
    yield web_driver
    web_driver.quit()
