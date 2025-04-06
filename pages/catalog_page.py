from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class CatalogPage(BasePage):
    URL = "/en-gb/catalog"
    DESKTOPS_CATALOG = (By.CSS_SELECTOR, "div.list-group.mb-3 a[href*='desktops']")
    LAPTOPS_CATALOG = (By.CSS_SELECTOR, "div.list-group.mb-3 a[href*='laptop-notebook']")
    COMPONENTS_CATALOG = (By.CSS_SELECTOR, "div.list-group.mb-3 a[href*='component']")
    TABLETS_CATALOG = (By.CSS_SELECTOR, "div.list-group.mb-3 a[href*='tablet']")
    SOFTWARE_CATALOG = (By.CSS_SELECTOR, "div.list-group.mb-3 a[href*='software']")
    SMARTPHONE_CATALOG = (By.CSS_SELECTOR, "div.list-group.mb-3 a[href*='smartphone']")
    CAMERAS_CATALOG = (By.CSS_SELECTOR, "div.list-group.mb-3 a[href*='cameras']")
    PLAYERS_CATALOG = (By.CSS_SELECTOR, "div.list-group.mb-3 a[href*='mp3-players']")
    CURRENCY_PRODUCT_CARD = (By.CSS_SELECTOR, ".row.row-cols-1 .col:first-child .product-thumb .price .price-new")
    CATALOG_ITEMS = {"Desktops": DESKTOPS_CATALOG, "Laptops": LAPTOPS_CATALOG, "Components": COMPONENTS_CATALOG,
                     "Tablets": TABLETS_CATALOG, "Software": SOFTWARE_CATALOG,
                     "Smartphone": SMARTPHONE_CATALOG, "Cameras": CAMERAS_CATALOG, "Players": PLAYERS_CATALOG}

    @allure.step("Открываем страницу каталога")
    def catalog_page_open(self, base_url):
        self.logger.info("Открываем страницу каталога")
        self.driver.get(base_url + self.URL)

    @allure.step("Проверяем наличие элемента каталога: {locator}")
    def is_catalog_item_present(self, locator, timeout=5):
        self.logger.info(f"Проверяем наличие элемента каталога: {locator}")
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            self.logger.warning(f"Элемент каталога {locator} не найден")
            return False

    @allure.step("Проверяем наличие всех элементов каталога")
    def are_all_catalog_items_present(self, timeout=5):
        self.logger.info("Проверяем наличие всех элементов каталога")
        wait = WebDriverWait(self.driver, timeout)
        missing_elements = []
        for name, locator in self.CATALOG_ITEMS.items():
            try:
                wait.until(EC.presence_of_element_located(locator))
                self.logger.info(f"Элемент найден: {name}")
            except:
                self.logger.error(f"Элемент отсутствует: {name}")
                missing_elements.append(name)
        if missing_elements:
            error_message = f"Отсутствуют элементы: {', '.join(missing_elements)}"
            self.logger.error(error_message)
            raise ValueError(error_message)

        return True