from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class AdminLoginPage(BasePage):
    URL = "/administration/"
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    MENU = (By.CSS_SELECTOR, "#menu-dashboard")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#nav-logout")

    @allure.step("Открываем страницу админки")
    def admin_page_open(self, base_url):
        self.logger.info("Открываем страницу админки:")
        self.driver.get(base_url + self.URL)

    @allure.step("Входим в админку под пользователем {username}")
    def login(self, username, password):
        self.logger.info(f"Вход в админку с логином: {username}")
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.logger.info("Нажимаем кнопку логина")
        self.find(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Проверяем, вошли ли в систему")
    def is_logged_in(self):
        self.logger.info("Проверяем, вошли ли в систему")
        return self.find(self.MENU)

    @allure.step("Выходим из админки")
    def logout(self):
        self.logger.info("Выход из админки")
        self.click(self.LOGOUT_BUTTON)

    @allure.step("Проверяем, вышли ли из системы")
    def is_logged_out(self):
        self.logger.info("Проверяем, вышли ли из системы")
        return self.find(self.LOGIN_BUTTON)