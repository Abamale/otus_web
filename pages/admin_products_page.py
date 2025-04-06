import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.admin_base_page import AdminBasePage
import allure

class AdminProductsPage(AdminBasePage):
    CATALOG_LINK = (By.CSS_SELECTOR, "a.parent.collapsed[href='#collapse-1']")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "#collapse-1 a[href*='catalog/product']")
    PRODUCTS_HEADER = (By.XPATH, "//h1[contains(text(), 'Products')]")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "[title='Add New']")
    ADD_PRODUCT_HEADER = (By.CSS_SELECTOR, ".card-header")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name-1")
    META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title-1")
    DATA_LINK = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    MODEL = (By.CSS_SELECTOR, "#input-model")
    SEO_LINK = (By.CSS_SELECTOR, 'a[href="#tab-seo"]')
    KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")
    SAVE_BUTTON = (By.CSS_SELECTOR, '.fa-solid.fa-floppy-disk')
    FILTER_PRODUCT_NAME = (By.CSS_SELECTOR, "[name='filter_name']")
    BUTTON_FILTER = (By.CSS_SELECTOR, "button[id='button-filter']")
    PRODUCT_LIST = (By.CSS_SELECTOR, "#form-product")
    BACK_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="Back"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, ".fa-regular.fa-trash-can")
    CHECKBOX = (By.CSS_SELECTOR, 'input.form-check-input[name="selected[]"]')
    SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success' and contains(text(), 'Success: You have modified products!')]")

    @allure.step("Открываем страницу управления товарами")
    def admin_products_page_open(self):
        self.logger.info("Открываем страницу управления товарами")
        self.click(self.CATALOG_LINK)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.PRODUCTS_LINK)  # Ожидание кликабельности
        )
        self.click(self.PRODUCTS_LINK)

    @allure.step("Проверяем, открылась ли страница товаров")
    def is_products_page_present(self, timeout=5):
        self.logger.info("Проверяем, открылась ли страница товаров")
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(self.PRODUCTS_HEADER))
            return True
        except:
            return False

    @allure.step("Открываем форму добавления нового товара")
    def add_new_product_form(self):
        self.logger.info("Открываем форму добавления нового товара")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_NEW_BUTTON)  # Ожидание кликабельности
        )
        self.click(self.ADD_NEW_BUTTON)

    @allure.step("Проверяем, открылась ли форма добавления товара")
    def is_new_product_form_present(self, timeout=5):
        self.logger.info("Проверяем, открылась ли форма добавления товара")
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(self.ADD_PRODUCT_HEADER))
            return True
        except:
            return False

    @allure.step("Добавляем новый товар")
    def add_new_product(self, fake_product):
        self.logger.info(f"Добавляем новый товар: {fake_product['product_name']}")
        self.add_new_product_form()
        self.send_keys(self.PRODUCT_NAME, fake_product["product_name"])
        self.send_keys(self.META_TAG_TITLE, fake_product["meta_tag_title"])
        self.click(self.DATA_LINK)
        self.send_keys(self.MODEL, fake_product["model"])
        self.click(self.SEO_LINK)
        self.send_keys(self.KEYWORD, fake_product["keyword"])
        self.logger.info("Сохраняем товар")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Проверяем, добавлен ли новый товар")
    def is_new_product_added(self, fake_product):
        self.logger.info(f"Проверяем, добавлен ли товар: {fake_product['product_name']}")
        self.click(self.PRODUCTS_LINK)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FILTER_PRODUCT_NAME))
        self.send_keys(self.FILTER_PRODUCT_NAME, fake_product["product_name"])
        self.click(self.BUTTON_FILTER)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(self.PRODUCT_LIST, f"{fake_product['product_name']}")
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Удаляем товар")
    def delete_product(self, fake_product):
        self.logger.info(f"Удаляем товар: {fake_product['product_name']}")
        self.click(self.PRODUCTS_LINK)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FILTER_PRODUCT_NAME))
        self.send_keys(self.FILTER_PRODUCT_NAME, fake_product["product_name"])
        self.click(self.BUTTON_FILTER)
        time.sleep(2)
        checkbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHECKBOX))
        self.driver.find_element(*self.CHECKBOX)
        self.driver.execute_script("arguments[0].checked = true;", checkbox)
        self.click(self.DELETE_BUTTON)
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()


    @allure.step("Проверяем, удален ли товар")
    def is_product_deleted(self, fake_product):
        self.logger.info(f"Проверяем, удален ли товар: {fake_product['product_name']}")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FILTER_PRODUCT_NAME))
        self.send_keys(self.FILTER_PRODUCT_NAME, fake_product["product_name"])
        self.click(self.BUTTON_FILTER)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(self.PRODUCT_LIST, "No results!")
            )
            return True
        except TimeoutException:
            return False
