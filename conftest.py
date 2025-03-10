import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from utils.data_generator import DataGenerator
from pages.catalog_page import CatalogPage
from pages.product_cart_page import ProductCartPage


def pytest_addoption(parser):
    load_dotenv()
    local_ip = os.getenv("LOCAL_IP")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome, firefox, edge")
    parser.addoption("--base-url", action="store", default=f"http://{local_ip}:8081", help="Base URL for OpenCart")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.fixture(scope="function")
def browser(request):
    browser_type = request.config.getoption("--browser")

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

@pytest.fixture
def fake_user():
    generator = DataGenerator()
    return generator.generate_user_data()

@pytest.fixture
def catalog_page(browser, base_url):
    catalog_page = CatalogPage(browser)
    catalog_page.catalog_page_open(base_url)
    return catalog_page

@pytest.fixture
def macbook_page(browser, base_url):
    macbook_page = ProductCartPage(browser)
    macbook_page.macbook_page_open(base_url)
    return macbook_page