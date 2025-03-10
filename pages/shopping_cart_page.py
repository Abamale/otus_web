from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ShoppingCart(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")
    SHOPPING_CART_TABLE = (By.CSS_SELECTOR, ".table-responsive")

    def is_shopping_cart_present(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False