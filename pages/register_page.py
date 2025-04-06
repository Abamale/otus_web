from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure

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

    @allure.step("Открываем страницу регистрации")
    def register_page_open(self, base_url):
        self.logger.info("Открываем страницу регистрации")
        self.driver.get(base_url + self.URL)

    @allure.step("Заполняем форму регистрации")
    def fill_registration_form(self, first_name, last_name, email, password):
        self.logger.info("Заполняем форму регистрации")
        self.send_keys(self.FIRST_NAME, first_name)
        self.logger.info(f"Вводим имя: {first_name}")
        self.send_keys(self.LAST_NAME, last_name)
        self.logger.info(f"Вводим фамилию: {last_name}")
        self.send_keys(self.EMAIL, email)
        self.logger.info(f"Вводим email: {email}")
        self.send_keys(self.PASSWORD, password)
        self.logger.info(f"Вводим пароль: {password}")
        self.click(self.PRIVACY_BUTTON)
        self.logger.info("Соглашаемся с условиями")
        self.click(self.CONTINUE_BUTTON)
        self.logger.info("Нажимаем кнопку 'Продолжить'")

    @allure.step("Проверяем, был ли создан аккаунт")
    def is_account_created_successfully(self):
        self.logger.info("Проверяем, был ли успешно создан аккаунт")
        return self.wait.until(
            EC.text_to_be_present_in_element(self.CONTENT_FIELD, "Your Account Has Been Created!")
        )