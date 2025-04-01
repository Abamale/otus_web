from pages.catalog_page import CatalogPage
from pages.home_page import HomePage
from utils.logger import logger
import allure


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия всех элементов каталога")
def test_are_all_catalog_items_present(catalog_page):
    logger.info("Проверка наличия всех элементов каталога")
    assert catalog_page.are_all_catalog_items_present(), "Некоторые элементы каталога отсутствуют!"


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия элемента каталога: 'Desktops'")
def test_is_desktop_catalog_present(catalog_page):
    logger.info("Проверка наличия каталога 'Desktops'")
    assert catalog_page.is_catalog_item_present(catalog_page.DESKTOPS_CATALOG)


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия элемента каталога: 'Laptops & Notebooks'")
def test_is_laptop_catalog_present(catalog_page):
    logger.info("Проверка наличия каталога 'Laptops & Notebooks'")
    assert catalog_page.is_catalog_item_present(catalog_page.LAPTOPS_CATALOG)


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия элемента каталога: 'Components'")
def test_is_components_catalog_present(catalog_page):
    logger.info("Проверка наличия каталога 'Components'")
    assert catalog_page.is_catalog_item_present(catalog_page.COMPONENTS_CATALOG)


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия элемента каталога: 'Tablets'")
def test_is_tablets_catalog_present(catalog_page):
    logger.info("Проверка наличия каталога 'Tablets'")
    assert catalog_page.is_catalog_item_present(catalog_page.TABLETS_CATALOG)


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия элемента каталога: 'Software'")
def test_is_software_catalog_present(catalog_page):
    logger.info("Проверка наличия каталога 'Software'")
    assert catalog_page.is_catalog_item_present(catalog_page.SOFTWARE_CATALOG)


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия элемента каталога: 'Phones & PDAs'")
def test_is_smartphone_catalog_present(catalog_page):
    logger.info("Проверка наличия каталога 'Phones & PDAs'")
    assert catalog_page.is_catalog_item_present(catalog_page.SMARTPHONE_CATALOG)


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия элемента каталога: 'Cameras'")
def test_is_cameras_catalog_present(catalog_page):
    logger.info("Проверка наличия каталога 'Cameras'")
    assert catalog_page.is_catalog_item_present(catalog_page.CAMERAS_CATALOG)


@allure.feature("Catalog")
@allure.story("Меню")
@allure.title("Проверка наличия элемента каталога: 'MP3 Players'")
def test_is_players_catalog_present(catalog_page):
    logger.info("Проверка наличия каталога 'MP3 Players'")
    assert catalog_page.is_catalog_item_present(catalog_page.PLAYERS_CATALOG)


@allure.feature("Catalog")
@allure.story("Изменение валюты")
@allure.title("Изменение валюты в каталоге на USD")
def test_changing_currency_usd_catalog(catalog_page):
    logger.info("Изменение валюты на USD и проверка в каталоге 'Desktops'")
    catalog_page.change_currency_usd()
    catalog_page.click(catalog_page.DESKTOPS_CATALOG)
    price_text = catalog_page.get_text(catalog_page.CURRENCY_PRODUCT_CARD)  # Получаем текст цены
    logger.info(f"Полученный текст цены: {price_text}")
    assert "$" in price_text, f"Currency symbol not found in: {price_text}"

