import allure
import pytest
from utils.schemas.auth import RegisterResponse, RegisterUnsuccessfulResponse
from utils.logger import logger
from tests.tests_api.test_data.auth_data import REGISTER_SUCCESS_DATA, REGISTER_UNSUCCESSFUL_DATA


@allure.feature("Авторизация - API Register")
@allure.story("Успешная регистрация - POST")
@allure.title("POST Register успешная регистрация с email={payload[email]}")
@pytest.mark.parametrize("payload", REGISTER_SUCCESS_DATA)
def test_register_success(api_client, payload):
    logger.info("Отправляем POST-запрос на регистрацию")
    response = api_client.post("register", json=payload)
    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200, f"Ожидался статус 200, получено: {response.status_code}"

    logger.info("Валидируем ответ с помощью Pydantic модели")
    validated_response = RegisterResponse(**response.json())

    logger.info("Проверяем, что вернулось id в ответе")
    assert isinstance(validated_response.id, int)
    logger.info("Проверяем, что вернулся token в ответе")
    assert isinstance(validated_response.token, str)


@allure.feature("Регистрация - API Register")
@allure.story("Неуспешная регистрация - POST")
@allure.title("Регистрация без пароля - ожидается ошибка")
@pytest.mark.parametrize("payload", REGISTER_UNSUCCESSFUL_DATA)
def test_register_unsuccessful(api_client, payload):
    logger.info(f"Отправляем POST-запрос на неуспешную регистрацию: {payload}")
    response = api_client.post("register", json=payload)

    logger.info("Проверяем статус-код 400")
    assert response.status_code == 400

    validated_response = RegisterUnsuccessfulResponse(**response.json())
    logger.info(f"Ответ API: {validated_response}")



