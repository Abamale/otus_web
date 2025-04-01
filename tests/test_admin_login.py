import os

import pytest
from utils.logger import logger
import allure


@allure.feature("Админка")
@allure.story("Авторизация")
@allure.title("Успешный вход в админку")
def test_admin_login(admin_login_page, admin_credentials):
    logger.info("Запуск теста на вход в админ-панель.")
    admin_login_page.login(admin_credentials["username"], admin_credentials["password"])
    assert admin_login_page.is_logged_in(), "Admin login failed"
    logger.info("Вход в админ-панель успешно выполнен.")


@allure.feature("Админка")
@allure.story("Авторизация")
@allure.title("Успешный выход из админки")
def test_admin_logout(admin_login_page, admin_credentials):
    logger.info("Запуск теста на выход из админ-панели.")
    admin_login_page.login(admin_credentials["username"], admin_credentials["password"])
    admin_login_page.logout()
    assert admin_login_page.is_logged_out()
    logger.info("Выход из админ-панели успешно выполнен.")

