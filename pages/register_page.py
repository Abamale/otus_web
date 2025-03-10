from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = "/en-gb?route=account/register"
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PRIVACY_BUTTON = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")
    CONTENT_FIELD = (By.CSS_SELECTOR, "#content")

    def register_page_open(self, base_url):
        self.driver.get(base_url + self.URL)

    def fill_registration_form(self, first_name, last_name, email, password):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.PRIVACY_BUTTON)
        self.click(self.CONTINUE_BUTTON)

    def is_account_created_successfully(self):
        return self.wait.until(
            EC.text_to_be_present_in_element(self.CONTENT_FIELD, "Your Account Has Been Created!")
        )