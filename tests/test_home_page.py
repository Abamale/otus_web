from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.shopping_cart_page import ShoppingCart


def test_changing_currency_usd(browser, base_url):
    page = HomePage(browser)
    page.open(base_url)
    page.change_currency_usd()
    price_text = page.get_text(page.CURRENCY_PRODUCT_CARD)  # Получаем текст цены
    assert "$" in price_text, f"Currency symbol not found in: {price_text}"


def test_add_product_to_cart(browser, base_url):
    home_page = HomePage(browser)
    home_page.open(base_url)
    first_product_name = home_page.find(home_page.NAME_OF_FIRST_CARD).text
    home_page.click_add_to_cart_button(home_page.ADD_TO_CART_BUTTON_FIRST)
    # Ожидание, пока кнопка "Добавить в корзину" станет кликабельной

    try:
        alert_close_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(home_page.ALERT_CLOSE_BUTTON)
        )
        alert_close_button.click()
    except TimeoutException:
        pass  # Если алерт не появился, продолжаем выполнение

    cart_page = ShoppingCart(browser)
    cart_page.shopping_cart_open()
    cart_content = cart_page.find(cart_page.SHOPPING_CART_TABLE).text

    assert first_product_name in cart_content, f"Товар '{first_product_name}' отсутствует в корзине!"