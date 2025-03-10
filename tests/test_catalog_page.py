from pages.catalog_page import CatalogPage
from pages.home_page import HomePage


def test_are_all_catalog_items_present(catalog_page):
    assert catalog_page.are_all_catalog_items_present(), "Некоторые элементы каталога отсутствуют!"

def test_is_desktop_catalog_present(catalog_page):
   assert catalog_page.is_catalog_item_present(catalog_page.DESKTOPS_CATALOG)

def test_is_laptop_catalog_present(catalog_page):
    assert catalog_page.is_catalog_item_present(catalog_page.LAPTOPS_CATALOG)

def test_is_components_catalog_present(catalog_page):
    assert catalog_page.is_catalog_item_present(catalog_page.COMPONENTS_CATALOG)

def test_is_tablets_catalog_present(catalog_page):
    assert catalog_page.is_catalog_item_present(catalog_page.TABLETS_CATALOG)

def test_is_software_catalog_present(catalog_page):
    assert catalog_page.is_catalog_item_present(catalog_page.SOFTWARE_CATALOG)

def test_is_smartphone_catalog_present(catalog_page):
    assert catalog_page.is_catalog_item_present(catalog_page.SMARTPHONE_CATALOG)

def test_is_cameras_catalog_present(catalog_page):
    assert catalog_page.is_catalog_item_present(catalog_page.CAMERAS_CATALOG)

def test_is_players_catalog_present(catalog_page):
    assert catalog_page.is_catalog_item_present(catalog_page.PLAYERS_CATALOG)

def test_changing_currency_usd_catalog(catalog_page):
    catalog_page.change_currency_usd()
    catalog_page.click(catalog_page.DESKTOPS_CATALOG)
    price_text = catalog_page.get_text(catalog_page.CURRENCY_PRODUCT_CARD)  # Получаем текст цены
    assert "$" in price_text, f"Currency symbol not found in: {price_text}"

