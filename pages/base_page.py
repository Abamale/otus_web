from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = setup_logger(self.__class__.__name__)

    CURRENCY_MENU = (By.CSS_SELECTOR, ".d-none.d-md-inline")
    CURRENCY_EUR = (By.CSS_SELECTOR, "ul.dropdown-menu.show a[href='EUR']")
    CURRENCY_GBP = (By.CSS_SELECTOR, "ul.dropdown-menu.show a[href='GBP']")
    CURRENCY_USD = (By.CSS_SELECTOR, "ul.dropdown-menu.show a[href='USD']")
    SHOPPING_CART = (By.CSS_SELECTOR, "a[title='Shopping Cart']")

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.logger.info(f"Открытие страницы: {url}")
        self.driver.get(url)

    @allure.step("Ищем элемент {locator}")
    def find(self, locator):
        self.logger.info(f"Поиск элемента: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликаем на элемент: {locator}")
    def click(self, locator):
        self.logger.info(f"Клик по элементу: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator))
        self.find(locator).click()

    @allure.step("Вводим текст: '{text}' в элемент: {locator}")
    def send_keys(self, locator, text):
        self.logger.info(f"Ввод текста '{text}' в элемент: {locator}")
        self.find(locator).send_keys(text)

    @allure.step("Получаем текст из элемента: {locator}")
    def get_text(self, locator):
        self.logger.info(f"Берем текст из: {locator}")
        return self.find(locator).text

    @allure.step("Закрываем страницу")
    def close(self):
        self.logger.info(f"Закрытие страницы")
        self.driver.quit()

    @allure.step("Меняем валюту на USD")
    def change_currency_usd(self):
        self.logger.info("Смена валюты на USD")
        self.click(self.CURRENCY_MENU)
        self.click(self.CURRENCY_USD)

    @allure.step("Меняем валюту на EUR")
    def change_currency_eur(self):
        self.logger.info("Смена валюты на EUR")
        self.click(self.CURRENCY_MENU)
        self.click(self.CURRENCY_EUR)

    @allure.step("Меняем валюту на GBP")
    def change_currency_gbp(self):
        self.logger.info("Смена валюты на GBP")
        self.click(self.CURRENCY_MENU)
        self.click(self.CURRENCY_GBP)

    @allure.step("Открываем корзину")
    def shopping_cart_open(self):
        self.logger.info("Открытие корзины")
        element = self.find(self.SHOPPING_CART)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        self.click(self.SHOPPING_CART)