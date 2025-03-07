from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    URL = "/administration/"
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    MENU = (By.CSS_SELECTOR, "#menu-dashboard")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#nav-logout")

    def admin_page_open(self, base_url):
        self.driver.get(base_url + self.URL)

    def login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_logged_in(self):
        return self.find(self.MENU)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def is_logged_out(self):
        return not self.find(self.MENU)