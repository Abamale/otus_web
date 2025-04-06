from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class AdminBasePage(BasePage):
    MENU = (By.CSS_SELECTOR, "#menu-dashboard")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#nav-logout")

    @allure.step("Проверяем, открыт ли дашборд")
    def is_dashboard_opened(self):
        self.logger.info("Проверяем, открыт ли дашборд")
        return self.find(self.MENU)

    @allure.step("Выходим из админки")
    def logout(self):
        self.logger.info("Выход из админки")
        self.click(self.LOGOUT_BUTTON)