from utils.logger import logger
import allure


@allure.feature("Админка. Catalog")
@allure.story("Products")
@allure.title("Отображение раздела с товарами: Products")
def test_is_product_page_present(product_page):
    logger.info("Запуск теста на проверку наличия страницы с товарами.")
    assert product_page.is_products_page_present(), "Страница с товарами не открыта"
    logger.info("Страница с товарами успешно открыта.")


@allure.feature("Админка. Catalog")
@allure.story("Products")
@allure.title("Добавление нового товара. Открытие карточки товара")
def test_new_product_form_present(product_page):
    logger.info("Запуск теста на проверку формы создания нового товара.")
    product_page.add_new_product_form()
    assert product_page.is_new_product_form_present(), "Форма карточки товара не открылась"
    logger.info("Форма карточки товара успешно открылась.")


@allure.feature("Админка. Catalog")
@allure.story("Products")
@allure.title("Добавление нового товара. Успешное добавление нового товара с минимальными полями")
def test_is_new_product_added(product_page, fake_product):
    logger.info("Запуск теста на добавление нового товара.")
    product_page.add_new_product(fake_product)
    assert product_page.is_new_product_added(fake_product), "Товар не создан"
    logger.info("Товар успешно добавлен.")


@allure.feature("Админка. Catalog")
@allure.story("Products")
@allure.title("Удаление товара. Успешное удаление товара")
def test_is_product_deleted(product_page, fake_product):
    logger.info("Запуск теста на удаление товара.")
    product_page.add_new_product(fake_product)
    product_page.delete_product(fake_product)
    assert product_page.is_product_deleted(fake_product), "Товар не был удален"
    logger.info("Товар успешно удален.")

@allure.feature("Админка. Catalog")
@allure.story("Products")
@allure.title("Специальный тест на проверку скриншота")
def test_fail_wrong_locator(product_page):
    product_page.click(product_page.SUCCESS_ALERT)  # Неверный локатор