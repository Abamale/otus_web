from pages.register_page import RegisterPage
from utils.logger import logger
import allure


@allure.feature("Home page")
@allure.story("Регистрация пользователя")
@allure.title("Успешная регистрация нового пользователя с минимальными полями")
def test_registration_success(browser, base_url, fake_user):
    logger.info("Регистрация нового пользователя")
    page = RegisterPage(browser)
    page.register_page_open(base_url)
    logger.info("Заполнение формы регистрации")
    page.fill_registration_form(
        fake_user["first_name"],
        fake_user["last_name"],
        fake_user["email"],
        fake_user["password"],
    )
    logger.info("Проверка успешного создания аккаунта")
    assert page.is_account_created_successfully(), "Account creation message not found!"