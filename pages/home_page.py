from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
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


