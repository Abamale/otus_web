from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class ProductCartPage(BasePage):
    URL = "/en-gb/product/macbook"
    BREADCRUMB_MACBOOK = (By.CSS_SELECTOR, "li.breadcrumb-item > a[href*='product/macbook']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-new")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, "button[formaction*='wishlist.add']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg.btn-block")

    @allure.step("Открываем страницу товара MacBook")
    def macbook_page_open(self, base_url):
        self.logger.info("Открываем страницу товара MacBook")
        self.driver.get(base_url + self.URL)

    @allure.step("Проверяем наличие элемента корзины: {locator}")
    def is_product_cart_present(self, locator, timeout=5):
        self.logger.info(f"Проверяем наличие элемента корзины по локатору: {locator}")
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"Элемент найден: {locator}")
            return True
        except:
            self.logger.error(f"Элемент не найден: {locator}")
            return False

    @allure.step("Получаем имя продукта")
    def get_product_name(self, locator):
        self.logger.info(f"Получаем имя продукта по локатору: {locator}")
        product_name_element = self.get_text(locator)
        return product_name_element

    @allure.step("Получаем цену продукта")
    def get_product_price(self):
        self.logger.info("Получаем цену продукта")
        product_price = self.find(self.PRODUCT_PRICE)
        return product_price

    @allure.step("Получаем кнопку 'Добавить в список желаемого'")
    def get_wishlist_button(self):
        self.logger.info("Получаем кнопку 'Добавить в список желаемого'")
        wishlist_button = self.find(self.WISHLIST_BUTTON)
        return wishlist_button

    @allure.step("Получаем кнопку 'Добавить в корзину'")
    def get_add_to_cart_button(self):
        self.logger.info("Получаем кнопку 'Добавить в корзину'")
        add_to_cart_button = self.find(self.ADD_TO_CART_BUTTON)
        return add_to_cart_button