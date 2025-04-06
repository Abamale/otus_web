from utils.logger import logger
import allure


@allure.feature("Product cart")
@allure.story("Карточка товара")
@allure.title("Открытие карточки товара")
def test_is_product_cart_present(macbook_page):
    logger.info("Проверка наличия MacBook на странице")
    assert macbook_page.is_product_cart_present(macbook_page.BREADCRUMB_MACBOOK)


@allure.feature("Product cart")
@allure.story("Карточка товара")
@allure.title("Отображение названия товара")
def test_product_name(macbook_page):
    logger.info("Проверка названия продукта")
    product_name_text = macbook_page.get_product_name(macbook_page.PRODUCT_NAME)
    logger.info(f"Полученное название: {product_name_text}")
    assert product_name_text == "MacBook", f"Ожидалось 'MacBook', но найдено '{product_name_text}'"


@allure.feature("Product cart")
@allure.story("Карточка товара")
@allure.title("Отображение цены товара")
def test_get_product_price(macbook_page):
    logger.info("Проверка отображения цены продукта")
    product_price = macbook_page.get_product_price()
    assert product_price.is_displayed(), "Цена продукта не отображается на странице!"


@allure.feature("Product cart")
@allure.story("Карточка товара")
@allure.title("Наличие кнопки добавления в избранное")
def test_get_wishlist_button(macbook_page):
    logger.info("Проверка наличия кнопки добавления в избранное")
    wishlist_button = macbook_page.get_wishlist_button()
    assert wishlist_button.is_displayed(), "Кнопка добавления в избранное не появилась на странице!"


@allure.feature("Product cart")
@allure.story("Карточка товара")
@allure.title("Наличие кнопки добавления в корзину")
def test_get_add_to_cart_button(macbook_page):
    logger.info("Проверка наличия кнопки добавления в корзину")
    add_to_cart_button = macbook_page.get_add_to_cart_button()
    assert add_to_cart_button.is_displayed(), "Кнопка добавления в корзину не появилась на странице!"