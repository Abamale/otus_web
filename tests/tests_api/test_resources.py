import allure
import pytest
from utils.schemas.resources import ResourceListResponse, SingleResourceResponse
from utils.logger import logger
from tests.tests_api.test_data.resources_data import EXISTING_RESOURCE_IDS, NOT_FOUND_RESOURCE_IDS


@allure.feature("Работа с ресурсами - API Resource")
@allure.story("Получение списка ресурсов - GET List")
@allure.title("Получение списка всех ресурсов")
def test_get_resource_list(api_client):
    logger.info("Отправляем GET-запрос на получение списка ресурсов")
    response = api_client.get("unknown")  # Для reqres - endpoint для ресурса это 'unknown'

    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200, (
        f"Ожидался статус 200, получено: {response.status_code}"
    )

    logger.info("Валидируем ответ с помощью Pydantic модели")
    validated_response = ResourceListResponse(**response.json())

    logger.info("Проверяем, что ответ не пустой")
    assert validated_response.data, "Ожидался непустой список ресурсов"
    for resource in validated_response.data:
        assert resource.id > 0


@allure.feature("Работа с ресурсами - API Resources")
@allure.story("Проверка соответствия per_page и длины data - GET")
@allure.title("Количество ресурсов соответствует значению per_page")
def test_resources_per_page_matches_data_length(api_client):
    logger.info("Отправляем GET-запрос на получение списка ресурсов")
    response = api_client.get("unknown")
    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    logger.info("Валидируем ответ с помощью Pydantic модели")
    validated_response = ResourceListResponse(**response.json())

    actual_count = len(validated_response.data)
    expected_count = validated_response.per_page

    logger.info("Проверяем, что количество ресурсов соответствует значению per_page")
    assert actual_count == expected_count, (
        f"Expected {expected_count} resources per page, got {actual_count}"
    )


@allure.feature("Работа с ресурсами - API Resources")
@allure.story("Проверка поля support.url - GET")
@allure.title("Поле support.url начинается с https://")
def test_support_url_starts_with_https(api_client):
    logger.info("Отправляем GET-запрос на получение списка ресурсов")
    response = api_client.get("unknown")
    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    logger.info("Валидируем ответ с помощью Pydantic модели")
    validated_response = ResourceListResponse(**response.json())

    support_url = validated_response.support.url

    logger.info("Проверяем, что поле support.url начинается с https://")
    assert support_url.startswith("https://"), (
        f"Ожидался URL, начинающийся с 'https://', получено: {support_url}"
    )


@allure.feature("Работа с ресурсами - API Resources")
@allure.story("Получение одного ресурса - GET")
@allure.title("GET Single Resource: Проверка id и статус-кода")
@pytest.mark.parametrize("resource_id", EXISTING_RESOURCE_IDS)
def test_get_single_resource(api_client, resource_id):
    logger.info("Отправляем GET-запрос на получение одного ресурса")
    response = api_client.get(f"unknown/{resource_id}")
    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    logger.info("Валидируем ответ с помощью Pydantic модели")
    validated_response = SingleResourceResponse(**response.json())

    logger.info("Проверяем, что id полученного ресурса соответствует запрошенному")
    assert validated_response.data.id == resource_id, (
        f"Ожидался id={resource_id}, получено: id={validated_response.data.id}"
    )


@allure.feature("Работа с ресурсами - API Resources")
@allure.story("Получение одного ресурса - не найдено - GET")
@allure.title("GET Single Resource Not Found: Проверка статус-кода 404 для id={resource_id}")
@pytest.mark.parametrize("resource_id", NOT_FOUND_RESOURCE_IDS)
def test_single_resource_not_found(api_client, resource_id):
    logger.info("Отправляем GET-запрос на получение одного ресурса")
    response = api_client.get(f"unknown/{resource_id}")
    logger.info("Проверяем статус-код 404")
    assert response.status_code == 404, f"Ожидался статус 404, получено: {response.status_code}"