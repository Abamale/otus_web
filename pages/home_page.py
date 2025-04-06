from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common import TimeoutException
from pages.shopping_cart_page import ShoppingCart
import allure

class HomePage(BasePage):
    SEARCH_FIELD = (By.NAME, "search")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    CURRENCY_PRODUCT_CARD = (By.CSS_SELECTOR, ".row.row-cols-1 .col:first-child .product-thumb .price .price-new")
    ADD_TO_CART_BUTTON_FIRST = (By.XPATH, "(//div[@class='product-thumb'])[1]//button[contains(@formaction, 'cart.add')]")
    NAME_OF_FIRST_CARD = (By.XPATH, "(//div[@class='product-thumb']//div[@class='description']/h4/a)[1]")
    ALERT_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'alert-dismissible')]//button[@class='btn-close']")


    @allure.step("Ищем товар с запросом: {query}")
    def search_product(self, query):
        self.logger.info(f"Ищем продукт с запросом: {query}")
        self.send_keys(self.SEARCH_FIELD, query)

    @allure.step("Добавляем товар в корзину")
    def click_add_to_cart_button(self, locator):
        self.logger.info(f"Нажимаем кнопку 'Добавить в корзину' для первого товара")
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        self.click(locator)
        self.logger.info(f"Продукт добавлен в корзину: {locator}")

    @allure.step("Меняем валюту на USD на главной странице")
    def changing_currency_usd_home(self):
        self.logger.info("Изменение валюты на USD и проверка на главной странице")
        self.change_currency_usd()
        price_text = self.get_text(self.CURRENCY_PRODUCT_CARD)  # Получаем текст цены
        self.logger.info(f"Полученный текст цены: {price_text}")
        return price_text

    @allure.step("Добавляем товар в корзину")
    def add_product_to_cart(self, browser):
        self.logger.info("Добавление товара в корзину и проверка его наличия")
        first_product_name = self.find(self.NAME_OF_FIRST_CARD).text
        self.logger.info(f"Название товара: {first_product_name}")
        self.click_add_to_cart_button(self.ADD_TO_CART_BUTTON_FIRST)
        # Ожидание, пока кнопка "Добавить в корзину" станет кликабельной

        try:
            self.logger.info("Ожидание закрытия алерта")
            alert_close_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable(self.ALERT_CLOSE_BUTTON)
            )
            alert_close_button.click()
        except TimeoutException:
            self.logger.warning("Алерт не появился, продолжаем выполнение")

        cart_page = ShoppingCart(browser)
        cart_page.shopping_cart_open()
        cart_content = cart_page.find(cart_page.SHOPPING_CART_TABLE).text
        self.logger.info(f"Содержимое корзины: {cart_content}")
        return first_product_name, cart_content