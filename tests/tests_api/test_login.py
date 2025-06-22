import allure
import pytest
from utils.schemas.auth import LoginResponse, LoginUnsuccessfulResponse
from utils.logger import logger
from tests.tests_api.test_data.auth_data import LOGIN_SUCCESS_DATA, LOGIN_UNSUCCESS_DATA


@allure.feature("Логин - API Login")
@allure.story("Успешный логин - POST")
@allure.title("Успешный логин пользователя")
@pytest.mark.parametrize("payload", LOGIN_SUCCESS_DATA)
def test_login_successful(api_client, payload):
    logger.info(f"Отправляем POST-запрос на успешный логин: {payload}")
    response = api_client.post("login", json=payload)

    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200

    logger.info("Валидируем ответ")
    validated_response = LoginResponse(**response.json())

    logger.info("Дополнительно проверяем, что токен - строка")
    assert isinstance(validated_response.token, str)


@allure.feature("Логин - API Login")
@allure.story("Неуспешный логин - POST")
@allure.title("Неуспешный логин пользователя без пароля")
@pytest.mark.parametrize("payload", LOGIN_UNSUCCESS_DATA)
def test_login_unsuccessful(api_client, payload):
    logger.info(f"Отправляем POST-запрос на неуспешный логин: {payload}")
    response = api_client.post("login", json=payload)

    logger.info("Проверяем статус-код 400")
    assert response.status_code == 400

    logger.info("Валидируем ответ")
    validated_response = LoginUnsuccessfulResponse(**response.json())

    logger.info("Проверяем точный текст ошибки")
    assert validated_response.error == "Missing password"

