from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.shopping_cart_page import ShoppingCart
from utils.logger import logger
import allure


@allure.feature("Home page")
@allure.story("Изменение валюты")
@allure.title("Изменение валюты на главной странице на USD")
def test_changing_currency_usd(browser, base_url):
    logger.info("Изменение валюты на USD и проверка на главной странице")
    page = HomePage(browser)
    page.open(base_url)
    page.change_currency_usd()
    price_text = page.get_text(page.CURRENCY_PRODUCT_CARD)  # Получаем текст цены
    logger.info(f"Полученный текст цены: {price_text}")
    assert "$" in price_text, f"Currency symbol not found in: {price_text}"


@allure.feature("Home page")
@allure.story("Корзина покупок")
@allure.title("Добавление товара в корзину с главной страницы")
def test_add_product_to_cart(browser, base_url):
    logger.info("Добавление товара в корзину и проверка его наличия")
    home_page = HomePage(browser)
    home_page.open(base_url)
    first_product_name = home_page.find(home_page.NAME_OF_FIRST_CARD).text
    logger.info(f"Название товара: {first_product_name}")
    home_page.click_add_to_cart_button(home_page.ADD_TO_CART_BUTTON_FIRST)
    # Ожидание, пока кнопка "Добавить в корзину" станет кликабельной

    try:
        logger.info("Ожидание закрытия алерта")
        alert_close_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(home_page.ALERT_CLOSE_BUTTON)
        )
        alert_close_button.click()
    except TimeoutException:
        logger.warning("Алерт не появился, продолжаем выполнение")

    cart_page = ShoppingCart(browser)
    cart_page.shopping_cart_open()
    cart_content = cart_page.find(cart_page.SHOPPING_CART_TABLE).text
    logger.info(f"Содержимое корзины: {cart_content}")

    assert first_product_name in cart_content, f"Товар '{first_product_name}' отсутствует в корзине!"