import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome, firefox, edge")
    parser.addoption("--base-url", action="store", default="http://localhost:8081", help="Base URL for OpenCart")


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url")

@pytest.fixture(scope="function")
def browser(pytestconfig):
    browser_type = pytestconfig.getoption("--browser")

    if browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def page(browser, base_url):
    browser.get(base_url)
    yield browser


@pytest.fixture(scope="session")
def admin_credentials():
    load_dotenv()
    return {
        "username": os.getenv("OPENCART_USERNAME"),
        "password": os.getenv("OPENCART_PASSWORD")
    }