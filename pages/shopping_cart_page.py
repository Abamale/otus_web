from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class ShoppingCart(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")
    SHOPPING_CART_TABLE = (By.CSS_SELECTOR, ".table-responsive")

    @allure.step("Проверяем, отображается ли корзина на странице")
    def is_shopping_cart_present(self, locator, timeout=5):
        self.logger.info("Проверяем, отображается ли корзина на странице")
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            self.logger.info("Корзина отображается на странице")
            return True
        except:
            self.logger.warning("Корзина не отображается на странице")
            return False