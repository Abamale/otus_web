from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    CURRENCY_MENU = (By.CSS_SELECTOR, ".d-none.d-md-inline")
    CURRENCY_EUR = (By.CSS_SELECTOR, "ul.dropdown-menu.show a[href='EUR']")
    CURRENCY_GBP = (By.CSS_SELECTOR, "ul.dropdown-menu.show a[href='GBP']")
    CURRENCY_USD = (By.CSS_SELECTOR, "ul.dropdown-menu.show a[href='USD']")
    SHOPPING_CART = (By.CSS_SELECTOR, "a[title='Shopping Cart']")

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def close(self):
        self.driver.quit()

    def change_currency_usd(self):
        self.click(self.CURRENCY_MENU)
        self.click(self.CURRENCY_USD)

    def change_currency_eur(self):
        self.click(self.CURRENCY_MENU)
        self.click(self.CURRENCY_EUR)

    def change_currency_gbp(self):
        self.click(self.CURRENCY_MENU)
        self.click(self.CURRENCY_GBP)

    def shopping_cart_open(self):
        element = self.find(self.SHOPPING_CART)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        self.click(self.SHOPPING_CART)