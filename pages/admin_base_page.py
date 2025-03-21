from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AdminBasePage(BasePage):
    MENU = (By.CSS_SELECTOR, "#menu-dashboard")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#nav-logout")

    def is_dashboard_opened(self):
        return self.find(self.MENU)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)