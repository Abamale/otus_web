from conftest import catalog_page
from pages.product_cart_page import ProductCartPage

def test_is_product_cart_present(macbook_page):
    assert macbook_page.is_product_cart_present(macbook_page.BREADCRUMB_MACBOOK)

def test_product_name(macbook_page):
    product_name_text = macbook_page.get_product_name(macbook_page.PRODUCT_NAME)
    assert product_name_text == "MacBook", f"Ожидалось 'MacBook', но найдено '{product_name_text}'"

def test_get_product_price(macbook_page):
    product_price = macbook_page.get_product_price()
    assert product_price.is_displayed(), "Цена продукта не отображается на странице!"

def test_get_wishlist_button(macbook_page):
    wishlist_button = macbook_page.get_wishlist_button()
    assert wishlist_button.is_displayed(), "Кнопка добавления в избранное не появилась на странице!"

def test_get_add_to_cart_button(macbook_page):
    add_to_cart_button = macbook_page.get_add_to_cart_button()
    assert add_to_cart_button.is_displayed(), "Кнопка добавления в корзину не появилась на странице!"