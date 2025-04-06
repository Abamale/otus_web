from utils.logger import logger
import allure


@allure.feature("Home page")
@allure.story("Изменение валюты")
@allure.title("Изменение валюты на главной странице на USD")
def test_changing_currency_usd(home_page):
    logger.info("Запуск теста на проверку изменения валюты товара на USD на главной странице")
    price_text = home_page.changing_currency_usd_home()
    assert "$" in price_text, f"Currency symbol not found in: {price_text}"


@allure.feature("Home page")
@allure.story("Корзина покупок")
@allure.title("Добавление товара в корзину с главной страницы")
def test_add_product_to_cart(home_page, browser):
    logger.info("Запуск теста на проверку добавления товара в корзину")
    product_name, cart_content = home_page.add_product_to_cart(browser)
    assert product_name in cart_content, f"Продукт '{product_name}' не найден в корзине: {cart_content}"
