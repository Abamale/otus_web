import pytest
from utils.schemas.users import UserListResponse, SingleUserResponse, UserCreateResponse, UserUpdateResponse
from utils.schemas.negative_response import NegativeResponse
from tests.tests_api.test_data.users_data import (POSITIVE_PAGES, NEGATIVE_PAGES, PAGE_TEST_DATA, EMAIL_REGEX,
                                                  AVATAR_URL_PREFIX, EXISTING_USER_IDS, NOT_FOUND_USER_IDS,
                                                  CREATE_USER_TEST_DATA, UPDATE_USER_TEST_DATA)

from utils.logger import logger
import allure


@allure.feature("Работа с пользователями - API Users")
@allure.story("Проверка валидных страниц пользователей - GET")
@allure.title("Проверка страницы {page_num} (позитивный тест)")
@pytest.mark.parametrize("page_num", POSITIVE_PAGES)
def test_positive_pages(api_client, page_num):
    logger.info(f"Отправляем GET-запрос для страницы {page_num}")
    response = api_client.get("users", params={"page": page_num})

    logger.info("Прверяем статус-код")
    assert response.status_code == 200, (
        f"Неверный статус код: {response.status_code}\nТело: {response.text}"
    )
    logger.info("Валидируем ответ")
    response_data = UserListResponse(**response.json())

    logger.info(f"Проверяем соответствие номера страницы: ожидается {page_num}, получено {response_data.page}")
    assert response_data.page == page_num, (
        f"Ожидалась страница {page_num}, но получена {response_data.page}"
    )



@allure.feature("Работа с пользователями - API Users")
@allure.story("Проверка невалидных страниц пользователей - GET")
@allure.title("Проверка страницы {page_num} (негативный тест)")
@pytest.mark.parametrize("page_num", NEGATIVE_PAGES)
def test_negative_pages(api_client, page_num):
    logger.info(f"Отправляем GET-запрос для страницы {page_num}")
    response = api_client.get("users", params={"page": page_num})

    logger.info("Проверяем статус-код")
    assert response.status_code == 401 or response.status_code == 404, (
        f"Ожидался код ошибки (401 или 404), но получен: {response.status_code}\nТело: {response.text}"
    )

    logger.info("Валидируем ответ")
    response_data = NegativeResponse(**response.json())

    logger.info("Проверяем сообщение об ошибке")
    assert response_data.error == "Missing API key.", (
        f"Ожидалась ошибка 'Missing API key.', но получено: {response_data.error}"
    )



@allure.feature("Работа с пользователями - API Users")
@allure.story("Проверка согласованности per_page и количества пользователей - GET")
@allure.title("Проверка количества пользователей на странице {page_num}")
@pytest.mark.parametrize("page_num", PAGE_TEST_DATA)
def test_users_count_matches_per_page(api_client, page_num):
    logger.info(f"Отправляем GET-запрос для страницы {page_num}")
    response = api_client.get("users", params={"page": page_num})

    logger.info("Прверяем статус-код")
    assert response.status_code == 200, (
        f"Неверный статус код: {response.status_code}\nТело: {response.text}"
    )
    logger.info("Валидируем ответ")
    response_data = UserListResponse(**response.json())

    logger.info("Сравниваем количество пользователей с per_page")
    actual_users_count = len(response_data.data)
    expected_per_page = response_data.per_page

    assert actual_users_count == expected_per_page, (
        f"На странице {page_num} пользователей: {actual_users_count}, "
        f"а per_page = {expected_per_page}"
    )


@allure.feature("Работа с пользователями - API Users")
@allure.story("Проверка корректности email у пользователей - GET")
@allure.title("Проверка email всех пользователей на странице {page_num}")
@pytest.mark.parametrize("page_num", PAGE_TEST_DATA)
def test_all_users_email_valid(api_client, page_num):
    logger.info(f"Отправляем GET-запрос для страницы {page_num}")
    response = api_client.get("users", params={"page": page_num})

    logger.info("Проверяем статус-код")
    assert response.status_code == 200, f"Неверный статус код: {response.status_code}"

    logger.info("Валидируем и парсим ответ через pydantic")
    response_data = UserListResponse(**response.json())

    logger.info(f"Проверяем email у {len(response_data.data)} пользователей")
    for user in response_data.data:
        logger.info(f"Проверяем email: {user.email}")
        assert EMAIL_REGEX.fullmatch(user.email), f"Некорректный email: {user.email}"


@allure.feature("Работа с пользователями - API Users")
@allure.story("Проверка корректности avatar у пользователей - GET")
@allure.title("Проверка avatar всех пользователей на странице {page_num}")
@pytest.mark.parametrize("page_num", PAGE_TEST_DATA)
def test_all_users_avatar_valid(api_client, page_num):
    logger.info(f"Отправляем GET-запрос для страницы {page_num}")
    response = api_client.get("users", params={"page": page_num})

    logger.info("Проверяем статус-код")
    assert response.status_code == 200, f"Неверный статус код: {response.status_code}"

    logger.info("Валидируем и парсим ответ через pydantic")
    response_data = UserListResponse(**response.json())

    logger.info(f"Проверяем avatar у {len(response_data.data)} пользователей")
    for user in response_data.data:
        logger.info(f"Проверяем avatar: {user.avatar}")
        assert user.avatar.startswith(AVATAR_URL_PREFIX), f"Некорректный avatar URL: {user.avatar}"


@allure.feature("Работа с пользователями - API Users")
@allure.story("Проверка поля url в блоке support - GET")
@allure.title("Проверка поля support.url на странице {page_num}")
@pytest.mark.parametrize("page_num", PAGE_TEST_DATA)
def test_support_url_valid(api_client, page_num):
    logger.info(f"Отправляем GET-запрос для страницы {page_num}")
    response = api_client.get("users", params={"page": page_num})

    logger.info("Проверяем статус-код")
    assert response.status_code == 200, f"Неверный статус код: {response.status_code}"

    logger.info("Валидируем и парсим ответ через Pydantic")
    response_data = UserListResponse(**response.json())

    logger.info(f"Проверяем support.url: {response_data.support.url}")
    assert response_data.support.url.startswith("https://"), \
        f"Некорректный support.url: {response_data.support.url}"


@allure.feature("Работа с пользователями - API Users")
@allure.story("Проверка получения одного пользователя - GET")
@allure.title("Проверка данных одного пользователя с id={user_id}")
@pytest.mark.parametrize("user_id", EXISTING_USER_IDS)
def test_single_user(api_client, user_id):
    logger.info(f"Отправляем GET-запрос для одного пользователя с id={user_id}")
    response = api_client.get(f"users/{user_id}")

    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200, (
        f"Ожидался статус 200, получено: {response.status_code}"
    )

    logger.info("Валидируем ответ через Pydantic")
    response_data = SingleUserResponse(**response.json())

    logger.info("Проверяем, что id в data совпадает с user_id")
    assert response_data.data.id == user_id, (
        f"Ожидался id={user_id}, получено: {response_data.data.id}"
    )


@allure.feature("Работа с пользователями - API Users")
@allure.story("Проверка ошибки при запросе несуществующего пользователя - GET")
@allure.title("Проверка 404 для несуществующего пользователя с id={user_id}")
@pytest.mark.parametrize("user_id", NOT_FOUND_USER_IDS)
def test_single_user_not_found(api_client, user_id):
    logger.info(f"Отправляем GET-запрос для несуществующего пользователя с id={user_id}")
    response = api_client.get(f"users/{user_id}")

    logger.info("Проверяем статус-код 404")
    assert response.status_code == 404, (
        f"Ожидался статус 404, получено: {response.status_code}"
    )


@allure.feature("Работа с пользователями - API Users")
@allure.story("Создание нового пользователя - POST")
@allure.title("Создание пользователя name={name}, job={job}")
@pytest.mark.parametrize("name, job", CREATE_USER_TEST_DATA)
def test_create_user(api_client, name, job):
    payload = {"name": name, "job": job}

    logger.info(f"Отправляем POST-запрос на создание пользователя: {payload}")
    response = api_client.post("users", json=payload)

    logger.info("Проверяем статус-код 201")
    assert response.status_code == 201, (
        f"Ожидался статус 201, получено: {response.status_code}"
    )

    logger.info("Валидируем JSON через Pydantic")
    user = UserCreateResponse(**response.json())

    logger.info("Проверяем, что имя совпадают с отправленными")
    assert user.name == name, f"Имя не совпадает: {user.name} != {name}"
    logger.info("Проверяем, что работа совпадают с отправленными")
    assert user.job == job, f"Должность не совпадает: {user.job} != {job}"


@allure.feature("Работа с пользователями - API Users")
@allure.story("Обновление пользователя - PUT")
@allure.title("Обновление пользователя name={name}, job={job}")
@pytest.mark.parametrize("name, job", UPDATE_USER_TEST_DATA)
def test_update_user(api_client, name, job):
    payload = {"name": name, "job": job}

    logger.info(f"Отправляем PUT-запрос для обновления пользователя: {payload}")
    response = api_client.put("users/2", json=payload)

    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200, f"Ожидался статус 200, получено: {response.status_code}"

    logger.info("Валидируем JSON через Pydantic")
    parsed_response = UserUpdateResponse(**response.json())
    logger.info("Проверяем, что имя совпадают с отправленными")
    assert parsed_response.name == name
    logger.info("Проверяем, что работа совпадают с отправленными")
    assert parsed_response.job == job


@allure.feature("Работа с пользователями - API Users")
@allure.story("Частичное обновление пользователя - PATCH")
@allure.title("Частичное обновление пользователя name={name}, job={job}")
@pytest.mark.parametrize("name, job", UPDATE_USER_TEST_DATA)
def test_patch_user(api_client, name, job):
    payload = {"name": name, "job": job}

    logger.info(f"Отправляем PATCH-запрос для частичного обновления пользователя: {payload}")
    response = api_client.patch("users/2", json=payload)

    logger.info("Проверяем статус-код 200")
    assert response.status_code == 200, f"Ожидался статус 200, получено: {response.status_code}"

    logger.info("Валидируем JSON через Pydantic")
    parsed_response = UserUpdateResponse(**response.json())
    logger.info("Проверяем, что имя совпадают с отправленными")
    assert parsed_response.name == name
    logger.info("Проверяем, что работа совпадают с отправленными")
    assert parsed_response.job == job


@allure.feature("Работа с пользователями - API Users")
@allure.story("Удаление пользователя - DELETE")
@allure.title("Удаление пользователя с id={user_id}")
@pytest.mark.parametrize("user_id", EXISTING_USER_IDS)
def test_delete_user(api_client, user_id):
    logger.info(f"Отправляем DELETE-запрос для удаления пользователя с id={user_id}")
    response = api_client.delete(f"users/{user_id}")

    logger.info("Проверяем статус-код 204")
    assert response.status_code == 204, (
        f"Ожидался статус 204, получено: {response.status_code}"
    )