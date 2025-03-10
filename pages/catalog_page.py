from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

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

    def catalog_page_open(self, base_url):
        self.driver.get(base_url + self.URL)


    def is_catalog_item_present(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def are_all_catalog_items_present(self, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        missing_elements = []
        for name, locator in self.CATALOG_ITEMS.items():
            try:
                wait.until(EC.presence_of_element_located(locator))
            except:
                missing_elements.append(name)
        if missing_elements:
            raise ValueError(f"Отсутствуют элементы: {', '.join(missing_elements)}")

        return True