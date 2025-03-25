import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
import logging

from pages.admin_products_page import AdminProductsPage
from utils.data_generator import DataGenerator
from pages.catalog_page import CatalogPage
from pages.product_cart_page import ProductCartPage
from pages.admin_login_page import AdminLoginPage


def pytest_addoption(parser):
    load_dotenv()
    local_ip = os.getenv("LOCAL_IP")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome, firefox, edge")
    parser.addoption("--base-url", action="store", default=f"http://{local_ip}:8081", help="Base URL for OpenCart")

# @pytest.fixture(scope="session", autouse=True)
# def setup_logging():
#     """Настройка логирования для тестов"""
#     logger = logging.getLogger("TestLogger")
#     if not logger.hasHandlers():  # Избегаем дублирования обработчиков
#         logger.setLevel(logging.INFO)
#
#         # Логирование в файл
#         file_handler = logging.FileHandler("test_log.log", encoding="utf-8")
#         file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#         file_handler.setFormatter(file_formatter)
#
#         # Логирование в консоль
#         console_handler = logging.StreamHandler()
#         console_formatter = logging.Formatter("%(levelname)s: %(message)s")
#         console_handler.setFormatter(console_formatter)
#
#         logger.addHandler(file_handler)
#         logger.addHandler(console_handler)
#
#     yield logger  # Фикстура возвращает логгер для использования в тестах и PageObject
#
#     # Закрываем обработчики после завершения тестов
#     for handler in logger.handlers:
#         handler.close()


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

@pytest.fixture
def admin_login_page(browser, base_url):
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.admin_page_open(base_url)
    return admin_login_page

@pytest.fixture
def admin_browser(browser, base_url, admin_credentials):
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.admin_page_open(base_url)
    admin_login_page.login(admin_credentials["username"], admin_credentials["password"])
    return browser

@pytest.fixture
def product_page(admin_browser):
    products_page = AdminProductsPage(admin_browser)
    products_page.admin_products_page_open()
    return products_page

@pytest.fixture
def fake_product():
    generator = DataGenerator()
    return generator.generate_products_data()