from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductCartPage(BasePage):
    URL = "/en-gb/product/macbook"
    BREADCRUMB_MACBOOK = (By.CSS_SELECTOR, "li.breadcrumb-item > a[href*='product/macbook']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-new")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, "button[formaction*='wishlist.add']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg.btn-block")

    def macbook_page_open(self, base_url):
        self.driver.get(base_url + self.URL)

    def is_product_cart_present(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def get_product_name(self, locator):
        product_name_element = self.get_text(locator)
        return product_name_element

    def get_product_price(self):
        product_price = self.find(self.PRODUCT_PRICE)
        return product_price

    def get_wishlist_button(self):
        wishlist_button = self.find(self.WISHLIST_BUTTON)
        return wishlist_button

    def get_add_to_cart_button(self):
        add_to_cart_button = self.find(self.ADD_TO_CART_BUTTON)
        return add_to_cart_button