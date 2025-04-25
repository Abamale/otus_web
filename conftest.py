import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
import uuid

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utils.logger import logger
import allure

from pages.admin_products_page import AdminProductsPage
from utils.data_generator import DataGenerator
from pages.catalog_page import CatalogPage
from pages.product_cart_page import ProductCartPage
from pages.admin_login_page import AdminLoginPage
from pages.home_page import HomePage



def pytest_addoption(parser):
    load_dotenv()
    local_ip = os.getenv("LOCAL_IP")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome, firefox, edge")
    parser.addoption("--base-url", action="store", default=f"http://{local_ip}:8081", help="Base URL for OpenCart")
    parser.addoption("--remote", action="store_true", help="Use remote browser via Selenoid")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.fixture(scope="function")
def browser(request):
    load_dotenv()
    local_ip = os.getenv("LOCAL_IP")

    browser_type = request.config.getoption("--browser")
    use_remote = request.config.getoption("--remote")
    logger.info(f"Запуск браузера: {browser_type}")

    if use_remote:
        selenoid_url = f"http://{local_ip}:4444/wd/hub"

        # Устанавливаем нужные опции в зависимости от браузера
        if browser_type == "chrome":
            options = ChromeOptions()
            options.add_argument("--headless")  # Запуск в headless-режиме
            options.add_experimental_option("w3c", True)  # Поддержка W3C
            options.set_capability("enableVNC", True)
            options.set_capability("enableVideo", True)  # Включить видео
            options.set_capability("videoName", f"{uuid.uuid4()}.mp4")  # Уникальное имя для видео


        elif browser_type == "firefox":
            options = FirefoxOptions()
            options.headless = True  # Включение headless-режима
            options.set_capability("enableVNC", True)
            options.set_capability("enableVideo", True)  # Включить видео
            options.set_capability("videoName", f"{uuid.uuid4()}.mp4")


        elif browser_type == "edge":
            options = EdgeOptions()
            options.add_argument("--headless")  # Запуск в headless-режиме
            options.set_capability("enableVNC", True)
            options.set_capability("enableVideo", True)  # Включить видео
            options.set_capability("videoName", f"{uuid.uuid4()}.mp4")

        else:
            raise ValueError(f"Unsupported browser: {browser_type}")

            # Создаём драйвер с учётом опций
        driver = webdriver.Remote(command_executor=selenoid_url, options=options)

    else:
        # Локальный запуск браузера, без Selenoid
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
    logger.info(f"Браузер {browser_type} закрыт.")

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
    logger.info("Вход в админ-панель.")
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
def home_page(browser, base_url):
    home_page = HomePage(browser)
    home_page.open(base_url)
    return home_page

@pytest.fixture
def fake_product():
    generator = DataGenerator()
    return generator.generate_products_data()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Добавляем статус теста в item
    item.status = 'failed' if rep.outcome != 'passed' else 'passed'

    # Если тест упал, делаем скриншот
    if rep.failed:
        driver = item.funcargs.get("browser")  # Достаем браузер из фикстур
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="Ошибка", attachment_type=allure.attachment_type.PNG)

        test_name = item.name
        logger.error(f"Тест {test_name} провален! Скриншот сохранен в Allure-отчете.")