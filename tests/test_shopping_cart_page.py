from pages.shopping_cart_page import ShoppingCart
from utils.logger import logger
import allure


@allure.feature("Shopping cart")
@allure.story("Корзина покупок")
@allure.title("Проверка страницы корзины покупок")
def test_is_shopping_cart_present(browser, base_url):
    logger.info("Проверка наличия корзины покупок")
    page = ShoppingCart(browser)
    page.open(base_url)
    page.shopping_cart_open()
    assert page.is_shopping_cart_present(page.CONTENT), "Shopping cart content not found!"

