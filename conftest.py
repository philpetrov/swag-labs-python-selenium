import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# Load environment variables from .env file at the project root
load_dotenv()


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


@pytest.fixture(scope="session")
def standard_user_credentials():
    """
    Fixture to provide standard user credentials from environment variables.
    """
    username = os.getenv("STANDARD_USER_USERNAME")
    password = os.getenv("STANDARD_USER_PASSWORD")
    if not username or not password:
        pytest.fail("Standard user credentials (STANDARD_USER_USERNAME, STANDARD_USER_PASSWORD) not found in .env file.")
    return username, password

@pytest.fixture(scope="session")
def base_url():
    """
    Fixture to provide the base URL of the application under test.
    """
    url = os.getenv("BASE_URL")
    if not url:
        pytest.fail("BASE_URL is not defined in the .env file.")
    return url